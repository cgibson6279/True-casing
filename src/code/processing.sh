#!/bin/bash

#Execute entire data processing pipeline

set -eou pipefail

main() {
    ./data_prep.py news.2007.gz train.tok dev.tok test.tok
    ./get_features.py train.tok train.features
    ./get_features.py dev.tok dev.features
    ./get_features.py test.tok test.features
    ./mixed_case.py news.2007.gz mc.json
}

main