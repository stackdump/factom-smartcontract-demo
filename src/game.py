"""
This file module provides functions for playing a game of tic-tac-toe
on the factom blockchain

Each move is commited as an entry to a factom chain.
A new chain is created using a timestamp to differentiate it.

Each entry is signed using ed25519 see: https://github.com/warner/python-ed25519
"""
import os
import json
import time
import ed25519
import client as fct

EC1 = os.environ.get('EC1', 'EC3Hu1W7uMHf7CtSva1cMyr5rXKsu7rVqQtkJCDHqEV9dgh5FjAj')
""" Entry Credit Address - override w/ an environment variable """

FA1 = os.environ.get('FA1', 'FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q')
""" Factoid Address - override w/ an environment variable """

AUDIT_PROGRAM_SHA1='028b635a83df0bd54707fecd9d818edba5049b5a'
""" fake sha1 hash - in reality this should reference a Github commit/sha1 hash """

GAME_NAME = 'XO-' + str(time.time())
""" external_id defining specific to a given game """

CHAINID = os.environ.get('CHAINID', '')
""" chain ID that will be created if not provided """

MOVE_COUNTER = 0

def _signing_key(name, prefix='player'):
    """
    helper to load signing keys from filesystem
    NOTE: keys must already be present  see: ./src/gen_keys.py
    """
    keydata = open(prefix + name + "-secret-key","rb").read()
    return ed25519.SigningKey(keydata)

SIGNING_KEYS = {'X': _signing_key('X'), 'O': _signing_key('O') }
""" ed25519 keys for each player """

def _counter():
    """ count number of moves in a game """
    global MOVE_COUNTER
    MOVE_COUNTER += 1
    return MOVE_COUNTER

def initialize_chain(dry_run=False):
    """
    create a new factom chain
    NOTE:  set dry_run=True to skip  pushing data to factom during development
    """
    global DRY_RUN
    global CHAINID

    DRY_RUN = dry_run

    metadata = {
        'name': GAME_NAME,
        'audit_program': AUDIT_PROGRAM_SHA1,
        'PlayerX': 'pubkey',  # FIXME actually include the validation keys here
        'PlayerO': 'pubkey'
    }
    content = json.dumps(metadata)

    if CHAINID == '' and not DRY_RUN:
        data = fct.commit_chain(EC1, content, [GAME_NAME, 'TicTacToe'])
        CHAINID = data['chainid']
        print("=> created chain %s" % CHAINID)
    else:
        print("=> using existing chain %s" % CHAINID)

    return CHAINID

def sign(**event):
    """ sign event data """
    key = SIGNING_KEYS[event['player']]
    data = json.dumps(event)
    return  {
        'event': data,
        'sig': key.sign(bytes(data, 'utf-8')).hex()
    }

def verify(**payload):
    """ raises ed25519.BadSignatureError an exception on invalid signature """
    event = json.loads(payload['event'])
    verify_key = SIGNING_KEYS[event['player']].get_verifying_key()
    verify_key.verify(bytes.fromhex(payload['sig']), bytes(payload['event'], 'utf-8'))
    return True

def move(player, move):
    """ encode moves as chain entry"""
    payload = sign(player=player, move=move, seq=_counter())
    content = json.dumps(payload)
    print("=> move(%s)\n" % (content))

    if DRY_RUN:
        return
    print(fct.commit_entry(EC1, CHAINID, content, [GAME_NAME, player]))

def gameover(winner='None', result='Draw'):
    """ encode game over message into chain """
    payload = sign(player=winner, result=result, seq=_counter())
    content = json.dumps(payload)


    print("=> %s(%s)\n" % (result, content))

    if DRY_RUN:
        return

    print(fct.commit_entry(EC1, CHAINID, content, [GAME_NAME, winner]))

def pause(seconds=3):
    """ wait for chain entries to propagate """
    if not DRY_RUN:
        time.sleep(seconds) # wait for entries to be committed
