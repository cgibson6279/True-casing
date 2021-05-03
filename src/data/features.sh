#!/bin/bash

# Extracts features from train, dev, and test sets
# Run in directory containing data

set -eou pipefail
set -x

main() {
    ./code/get_features.py tok/train.tok features/train.features
    ./code/get_features.py tok/dev.tok features/dev.features
    ./code/get_test_features.py tok/test.tok features/test.features tok/cased_test.tok
}

main