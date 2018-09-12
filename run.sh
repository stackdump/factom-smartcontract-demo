#!/usr/bin/env bash

if [[ ! -f playerX-secret-key  ]] ; then
    python ./src/gen_keys.py
else
    echo using existing keys
fi

# simulate a game of tic-tac-toe
python ./src/play.py

# run the auditor
# FIXME
