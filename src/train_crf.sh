
#!/bin/bash

#Train the CRF model

set -eou pipefail

main() {
    # need to figure out how to pass paths to script
    crfsuite learn \
        -p feature.possible_states=1 \
        -p feature.possible_transitions=1 \
        -m model \
        -e2 data/train.features data/dev.features
}

main 