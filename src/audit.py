"""
this contains code that validates a game of tic-tac-toe played on factom blockchain
"""

import sys


print(sys.argv)
if len(sys.argv) == 1:
    raise Exception('must pass chainid as an arg to this program')

CHAINID = sys.argv[1]

import json
import client as fct
import game

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

entries = fct.get_all_entries(CHAINID)
player_moves = { 'X': [], 'O': [] } # data structure to classify X/O moves
allmoves = [] # hold a copy of all moves
gamedata = None
final_result = None

for entry in entries:
    payload = json.loads(entry['content'])

    if 'event' in payload:
        assert game.verify(**payload) # Validate Event Signatures
        event = json.loads(payload['event']) # deserialize event data

        if 'result' in event:
            # save final result for later validation
            final_result = event
        elif 'move' in event:
            # collect moves by player to be used later to verify Win Scenario
            player_moves[event['player']].append(event['move'])

            # collect a list of 
            allmoves.append(event)
    elif 'audit_program' in payload: # Found first chain entry
        gamedata = payload

# verify we are auditing w/ a correct program
assert gamedata['audit_program'] == game.AUDIT_PROGRAM_SHA1
print("GameInfo:\n", gamedata)

print("Moves:")
for event in allmoves:
    # validate that players did not play out of sequence
    if event['player'] == 'X':
        assert (event['seq'] % 2) == 1 # X has all odd moves
    elif event['player'] == 'O':
        assert (event['seq'] % 2) == 0 # O has all even moves

    # validate that no duplicate moves are found
    assert event['move'] in BOARD
    BOARD.remove(event['move'])
    print(event)


# check X & O Sets of moves against the WINNING_SETS to certify a win claim
if final_result['result'] == 'Win':

    valid_win = False

    for winset in WINNING_SETS:
        if winset.issubset(player_moves[final_result['player']]):
            valid_win = True

    # assert that the final result is valid
    assert valid_win

print("Final:\n", final_result)
