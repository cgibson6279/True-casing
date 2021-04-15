#!/usr/bin/env python
"""data_prep.py

Splits data into train, dev, and test sets
"""

import argparse
import gzip
import logging
import random

from typing import Iterator, List

def read_file(path: str) -> List[str]:
    """Read file opens .gz files and 
    .txt files and returns a list of strings
    """
    if path.endswith(".gz"):
        with gzip.GzipFile(path, "r") as src:
            lines = []
            for line in src:
                line = line.decode("utf-8").rstrip()
                lines.append(line.split())
        return lines
    else:
        with open(path, "r") as src:
            lines = []
            for line in src:
                line = line.decode("utf-8").rstrip()
                lines.append(line.split())
        return lines


def main(args: argparse.Namespace) -> None:
    # Read in file as list
    corpus = read_file(args.data)
    # Get values for splitting data
    train_size = int(len(corpus) * 0.8)
    dev_size = int(len(corpus) * 0.1)
    # Shuffle corpus
    random.Random(42).shuffle(corpus)
    # Split data into train, dev, test 
    train_data = corpus[:train_size]
    dev_data = corpus[train_size:train_size+dev_size]
    test_data = corpus[train_size+dev_size:]
    # Print data to files
    with open(args.train, "w") as out_file:
        for line in train_data:
            print(" ".join(line), file=out_file)
    with open(args.dev, "w") as out_file:
        for line in dev_data:
            print(" ".join(line), file=out_file)
    with open(args.test, "w") as out_file:
        for line in test_data:
            print(" ".join(line), file=out_file)
    # Log output
    logging.info(f"Train set = {len(train_data)}")
    logging.info(f"Dev set = {len(dev_data)}")
    logging.info(f"Test set = {len(test_data)}")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trains the case-restoration model")
    parser.add_argument("data", help="Path to input data file")
    parser.add_argument("train", help="Path for train data file")
    parser.add_argument("dev", help="Path for dev data file")
    parser.add_argument("test", help="Path for test data file")
    logging.basicConfig(level=logging.INFO)
    namespace = parser.parse_args()
    main(namespace)