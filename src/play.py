#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file module generates valid tic-tac-toe game moves
on the factom blockchain

Moves are encoded using coordinates + a Player 'X' or 'O'

    ┌───┬───┬───┐
    │00 │01 │02 │
    ├───┼───┼───┤
    │10 │11 │12 │
    ├───┼───┼───┤
    │20 │21 │22 │
    └───┴───┴───┘

"""
from game import initialize_chain, pause, move, gameover
# run a simulated game of tic-tac-toe

CHAINID = initialize_chain(dry_run=False)
# NOTE: adding a new chain costs 10 EC
# usually you would avoid this except in a development environment

pause(3) # wait for chain to be created

print('------------------')
move('X', '11')
print('------------------')
move('O', '02')
print('------------------')
move('X', '22')
print('------------------')
move('O', '00')
print('------------------')
move('X', '01')
print('------------------')
move('O', '10')
print('------------------')
move('X', '21')
print('------------------')
gameover('X', 'Win')
print('------------------')

pause(3) # wait for entries to propagate
print('Review blochain entries:')
print('http://127.0.0.1:8090/search?input=%s&type=chainhead' % CHAINID)
