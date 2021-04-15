#!/bin/bash
"""processing.sh

Execute entire data processing pipeline
"""
set -eou pipefail

read data

main() {
    ./data_prep.py $data train.tok dev.tok test.tok
    ./get_features.py train.tok train.features
    ./get_features.py dev.tok dev.features
    ./get_features.py test.tok test.features
    ./mixed_case $data mc.json
}

main