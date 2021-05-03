#!/usr/bin/env python
"""train.py

Generates feature file for given data set.
"""
import argparse

from nltk import word_tokenize
from typing import List


def _suffix_feature(token: str, size: int) -> str:
    return f"suf{size}={token[-size:].casefold()}"


def extract(tokens: List[str]) -> List[List[str]]:
    """Feature extraction."""
    # NB: tokens are assumed to already be case-folded.
    vectors = [[f"t[0]={str.casefold(token)}"] for token in tokens]
    # Edge features.
    vectors[0].append("__BOS__")
    vectors[-1].append("__EOS__")
    # Preceding and following word features.
    if len(tokens) > 1:
        for i in range(1, len(tokens) - 1):
            prev_token_feat = f"t[-1]={tokens[i - 1].casefold()}"
            next_token_feat = f"t[+1]={tokens[i + 1].casefold()}"
            vectors[i].append(prev_token_feat)
            vectors[i].append(next_token_feat)
            # Conjunction of the two.
            vectors[i].append(f"{prev_token_feat}^{next_token_feat}")
        if len(tokens) > 2:
            for i in range(2, len(tokens) - 2):
                vectors[i].append(f"t[-2]={tokens[i - 2].casefold()}")
                vectors[i].append(f"t[+2]={tokens[i + 2].casefold()}")
    # Suffix features.
    for (i, token) in enumerate(tokens):
        vector = vectors[i]
        if len(token) > 1:
            vector.append(_suffix_feature(token, 1))
            if len(token) > 2:
                vector.append(_suffix_feature(token, 2))
                if len(token) > 3:
                    vector.append(_suffix_feature(token, 3))
    # And we're done.
    return vectors


def main(args: argparse.Namespace) -> None:
    with open(args.data, "r") as src:
        with open(args.features, "w") as out_file:
            with open(args.cased, "w") as cased:
                with open(args.gold, "w") as gold:
                    for line in src:
                        line = word_tokenize(line.replace(":", "_"))
                        # Get features
                        feature_list = extract(line)
                        for feature in feature_list:
                            print("\t".join(feature), file=out_file)
                        print("", file=out_file)
                        # Make test casefolded tokens file
                        for word in line:
                            print(word.casefold(), file=cased)
                        print("", file=cased)
                        for word in line:
                            print(word, file=gold)
                        print("", file=gold)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Trains the case-restoration model"
    )
    parser.add_argument("data", help="Path to input data file.")
    parser.add_argument("features", help="Path for feature data file.")
    parser.add_argument(
        "cased", help="Path to file for writing casefolded test tokens."
    )
    parser.add_argument("gold", help="Path to file for writing gold tokens.")
    namespace = parser.parse_args()
    main(namespace)
