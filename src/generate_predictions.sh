#!/bin/bash

# Predict or restore case to the tokens in test.tok

set -eou pipefail
set -x

FILE=$1
main() {
    crfsuite tag -m model $FILE > data/test.predictions
}

main $FILE

