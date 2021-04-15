#!/bin/bash

# Execute entire data processing pipeline
# Run in directory containing data

set -eou pipefail

FILE=$1
main() {
    ./code/data_prep.py $FILE train.tok dev.tok test.tok
    ./code/get_features.py train.tok train.features
    ./code/get_features.py dev.tok dev.features
    ./code/get_test_features.py test.tok test.features
    ./code/mixed_case.py $FILE mc.json
}

main $FILE