#!/usr/bin/env python
"""train.py

Generates feature file for given data set.
"""
import argparse
import logging

import gzip
from nltk import word_tokenize
from typing import List, Tuple
import features 

def main(args: argparse.Namespace) -> None:
    with open(args.data, "r") as src:
        with open(args.features, "w") as out_file:
            for line in src:
                line = word_tokenize(line.replace(":","_"))
                feature_list = features.extract(line)
                for feature in feature_list:
                    print("\t".join(feature),file=out_file)
                print("\n", file=out_file)

            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trains the case-restoration model")
    parser.add_argument("data", help="Path to input data file")
    parser.add_argument("features", help="Path for feature data file")
    namespace = parser.parse_args()
    main(namespace)