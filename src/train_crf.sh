
#!/bin/bash

#Train the CRF model

set -eou pipefail

# need to figure out how to pass paths to script
crfsuite learn \
    -p feature.minfreq=5 \
    -p feature.possible_states=0 \
    -p feature.possible_transitions=0 \
    -m model \
    -a ap \
    -p max_iterations=20 \
    -e2 data/features/train.features data/features/dev.features