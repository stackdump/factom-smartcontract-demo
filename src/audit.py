"""
Incomplete - this contains code that would validate a game of tic-tac-toe
but the client.py doesn't yet implement the full API calls needed to retrieve all events
"""
CHAINID='8f7e2b82395b84491e50742957949278548d5de51596930e793d64c786881adb'

import client as fct

BOARD = ['00', '01', '02',
         '10', '11', '12',
         '20', '21', '22']

WINNING_SETS = (set(('00', '01', '02')),
                set(('10', '11', '12')),
                set(('20', '21', '22')),
                set(('00', '11', '22')),
                set(('02', '11', '20')),
                set(('00', '10', '20')),
                set(('01', '11', '21')),
                set(('02', '12', '22')))

print(fct.get_all_entries(CHAINID)) # FIXME this is not yet implemented

# TODO: get stream of events (all entries for a given chain)
# - check for duplicate moves
# - check for out of turn moves
# - divide events into X sets and O sets
#   - check X & O Sets of moves against the WINNING_SETS to certify a win claim
