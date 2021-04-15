#!/usr/bin/env python
"""train.py

Createes a JSON contain a mixed case dictionary 
"""
import argparse
import collections
import json
import logging

import gzip
from nltk import word_tokenize
import typing

import case
import features 

DATA_PATH = "/home/cgibson6279/Desktop/WinterCamp/src/data/"

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
        mc_dict[token.casefold()][token] += 1
    
    max_mc_dict=collections.defaultdict()
    for token in mc_dict.keys():
        max_mc_dict[token.casefold()] = mc_dict[token].most_common()
    
    with open(args.mixed_case, "w", encoding="utf-8") as out_file:
         json.dump(max_mc_dict, out_file, ensure_ascii=False, indent=4)
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trains the case-restoration model")
    parser.add_argument("input", help="Path to input data file")
    parser.add_argument("mixed_case", help="Path for write mixed case JSON")
    namespace = parser.parse_args()
    main(namespace)