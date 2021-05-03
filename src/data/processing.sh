#!/bin/bash

# Split data into test, train, split files and creates mixed dictionary
# Run in directory containing data

set -eou pipefail
set -x

FILE=$1
main() {
    #should echo some output that tracks progress
    ./code/data_prep.py $FILE tok/train.tok tok/dev.tok tok/test.tok
    ./code/mixed_case.py $FILE mc.json
}

main $FILE