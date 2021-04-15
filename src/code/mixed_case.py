#!/usr/bin/env python
"""train.py

Trains the case-restoration model
"""
import argparse
import collections
import json
import logging

import gzip
from nltk import word_tokenize
from typing import List, Tuple

import case
import features 

def main(args: argparse.Namespace) -> None:
    with gzip.GzipFile(args.input, "r") as src:
        mc_list = []
        for line in src:
            line = word_tokenize(line.decode("utf-8").replace(":","_"))
            for token in line:
                tc, pattern = case.get_tc(token)
                if tc == case.TokenCase.MIXED:
                    mc_list.append(token)
    # Create mixed case dict
    mc_dict = collections.defaultdict(collections.Counter)
    for token in mc_list:
        mcdict[token.casefold()][token] += 1



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trains the case-restoration model")
    parser.add_argument("input", help="Path to input data file")
    #parser.add_argument("mixed_case", help="Path for write data file")
    namespace = parser.parse_args()
    main(namespace)