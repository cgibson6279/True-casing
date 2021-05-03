#!/usr/bin/env python
"""Evaluates a language model."""
import argparse


def main(args: argparse.Namespace) -> None:
    with open(args.gold, "r") as gold:
        with open(args.pred, "r") as pred:
            correct = 0
            total = 0
            for (gold_line, pred_line) in zip(gold, pred):
                total += 1
                if pred_line == gold_line:
                    correct += 1
    with open(args.out, "w") as out_file:
        word_accuracy = round((correct / total) * 100, 2)
        print(f"Word Accuracy: {word_accuracy}", file=out_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Evaluates a case-restoration model."
    )
    parser.add_argument("gold", help="Path to gold token file.")
    parser.add_argument("pred", help="Path for test token data file.")
    parser.add_argument("out", help="Path to write evulation results.")
    namespace = parser.parse_args()
    main(namespace)
