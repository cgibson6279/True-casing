#!/usr/bin/env python
"""Apply casing to case-folded tokens in test.tok"""
import argparse

import json

from case import apply_tc, TokenCase


def main(args: argparse.Namespace) -> None:
    with open(args.tok, "r", encoding="UTF-8") as tok:
        with open(args.predictions, "r", encoding="UTF-8") as preds:
            with open(args.mcdict, "r") as mixed:
                with open(args.out, "w", encoding="UTF-8") as out_file:
                    mcdict = json.load(mixed, encoding="UTF-8")
                    word_list = []
                    pred_list = []
                    for word in tok:
                        word_list.append(word)
                    for pred in preds:
                        pred_list.append(pred)
                    if len(word_list) == len(word_list):
                        for i in range(len(word_list)):
                            if pred_list[i].rstrip() == "DC":
                                tc = TokenCase.DC
                            elif pred_list[i].rstrip() == "LOWER":
                                tc = TokenCase.LOWER
                            elif pred_list[i].rstrip() == "UPPER":
                                tc = TokenCase.UPPER
                            elif pred_list[i].rstrip() == "TITLE":
                                tc = TokenCase.TITLE
                            elif pred_list[i].rstrip() == "MIXED":
                                tc = TokenCase.MIXED
                            word = apply_tc(word_list[i], tc, mcdict).rstrip()
                            print(word, file=out_file)
                        print("", file=out_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Apply casing to case-folded tokens in test.tok."
    )
    parser.add_argument(
        "tok", help="Path to case folded tokens file for making predictions."
    )
    parser.add_argument("predictions", help="Path to predictions file")
    parser.add_argument("mcdict", help="Path to mixed cased dictionary file")
    parser.add_argument(
        "out", help="Path to file to write corrected case tokens."
    )
    namespace = parser.parse_args()
    main(namespace)
