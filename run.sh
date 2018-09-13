#!/usr/bin/env bash

if [[ ! -f playerX-secret-key  ]] ; then
    python ./src/gen_keys.py
else
    echo using existing keys
fi

# buy EC
factom-cli buyec FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q  EC3Hu1W7uMHf7CtSva1cMyr5rXKsu7rVqQtkJCDHqEV9dgh5FjAj  20

# simulate a game of tic-tac-toe
python ./src/play.py

echo ------------------
echo "run the auditor manually - NOTE: you must pass the new chain ID as a param"
echo "python src/audit.py <CHAINID>"
