"""
Provide a python API for many of the factom API calls

see: https://docs.factom.com/api for more details on both the wallet & factomd APIs
"""
import json # DEBUG
import requests
import time
import codecs

SLEEP = 2
FACTOM_URL = 'http://localhost:8088/v2'
WALLET_URL = 'http://localhost:8089/v2'
HEADERS = {'content-type' : 'application/json'}

ROOT_KEYMR = "0000000000000000000000000000000000000000000000000000000000000000"

def create_ec_address():
    """  Create a new EC address """
    data = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "generate-ec-address"
    }
    r = requests.post(WALLET_URL, json=data, headers=HEADERS)
    result_dict = r.json()
    return result_dict['result']['public']

def fct_to_ec(ec_address, tx_name, amount):
    """ Exchange Factoids for Entry Credits """
    data = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "new-transaction",
        "params": {
            "tx-name": tx_name
        }
    }
    r = requests.post(WALLET_URL, json=data, headers=HEADERS)
    data = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "add-input",
        "params":{
            "tx-name": tx_name,
            "address": "FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q",
            "amount": amount
        }
    }
    r = requests.post(WALLET_URL, json=data, headers=HEADERS)
    data = {
        "jsonrpc": "2.0",
        "id":0,
        "method": "add-ec-output",
        "params": {
            "tx-name": tx_name,
            "address": ec_address,
            "amount": amount
        }
    }
    r = requests.post(WALLET_URL, json=data, headers=HEADERS)
    data = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "add-fee",
        "params": {
            "tx-name": tx_name,
            "address": "FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q",
        }
    }
    r = requests.post(WALLET_URL, json=data, headers=HEADERS)
    data = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "sign-transaction",
        "params":{
            "tx-name": tx_name,
        }
    }
    r = requests.post(WALLET_URL, json=data, headers=HEADERS)
    data = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "compose-transaction",
        "params": {
            "tx-name": tx_name
        }
    }
    r = requests.post(WALLET_URL, json=data, headers=HEADERS)
    result_dict = r.json()
    r = requests.post(FACTOM_URL, json=result_dict['result'], headers=HEADERS)

def commit_chain(ec_address, content, external_ids):
    """ Create a new chain """
    commit,reveal = _get_commit_chain(ec_address, content, external_ids)
    r = requests.post(FACTOM_URL, json=commit, headers=HEADERS)
    time.sleep(SLEEP)
    r = requests.post(FACTOM_URL, json=reveal, headers=HEADERS)
    result_dict = r.json()
    return result_dict['result']

def _get_commit_chain(ec_address, content, external_ids):
    """ Helper for commit_chain to get commit-entry and reveal-entry API calls  """
    data = {
        "id": 0,
        "jsonrpc": "2.0",
        "method": "compose-chain",
        "params": {
            "chain": {
                "firstentry": {
                    "content": _hexencode(content),
                    "extids": [ _hexencode(_id) for _id in external_ids ] 
                }
            },
            "ecpub": ec_address
        }
    }
    r = requests.post(WALLET_URL, json=data, headers=HEADERS)
    result_dict = r.json()
    if 'result' not in result_dict:
        raise Exception(result_dict['error'])

    return result_dict['result']['commit'], result_dict['result']['reveal']

def commit_entry(ec_address, chainid, content, external_ids):
    """ Commit a new entry to the chain """
    commit,reveal = _get_commit_entry(ec_address, chainid, content, external_ids)
    r = requests.post(FACTOM_URL, json=commit, headers=HEADERS)
    time.sleep(SLEEP)
    r = requests.post(FACTOM_URL, json=reveal, headers=HEADERS)
    result_dict = r.json()
    return result_dict['result']

def _get_commit_entry(ec_address, chainid, content, external_ids):
    """ Helper for commit_entry to get commit-entry and reveal-entry API calls  """

    data = {
        "id": 0,
        "jsonrpc": "2.0",
        "method": "compose-entry",
        "params": {
            "ecpub": ec_address,
            "entry": {
                "content": _hexencode(content),
                "chainid": chainid,
                "extids": [ _hexencode(_id) for _id in external_ids ] 
            }
        }
    }
    r = requests.post(WALLET_URL, json=data, headers=HEADERS)
    result_dict = r.json()
    if 'result' not in result_dict:
        raise Exception(result_dict['error'])
    return result_dict['result']['commit'], result_dict['result']['reveal']



def get_entry(hash):
    """ Get an entry  """
    data = {
        "id": 0,
        "jsonrpc": "2.0",
        "method": "entry",
        "params": {
            "hash": hash
        }
    }
    r = requests.post(FACTOM_URL, json=data, headers=HEADERS)
    result_dict = r.json()

    if 'result' not in result_dict:
        raise Exception(result_dict['error'])

    result_dict['result']['content'] = _hexdecode(result_dict['result']['content'])
    result_dict['result']['extids'] = [ _hexdecode(_id) for _id in result_dict['result']['extids'] ]

    return result_dict['result']

def get_chain_head(chainid):
    """ Get chain head """
    data = {
        "id": 0,
        "jsonrpc": "2.0",
        "method": "chain-head",
        "params": {
            "chainid": chainid
        }
    }
    r = requests.post(FACTOM_URL, json=data, headers=HEADERS)
    result_dict = r.json()
    return result_dict['result']['chainhead']

def get_entry_block(chainhead):
    """ Get chain head """
    data = {
        "id": 0,
        "jsonrpc": "2.0",
        "method": "entry-block",
        "params": {
            "keymr": chainhead
        }
    }
    r = requests.post(FACTOM_URL, json=data, headers=HEADERS)
    result_dict = r.json()
    return result_dict['result']

def get_all_blocks(chainid):
    """ Get an entry  """
    chainhead = get_chain_head(chainid)
    blocks = []
    entry_block = get_entry_block(chainhead)
    blocks.append(entry_block)

    while entry_block['header']['prevkeymr'] != ROOT_KEYMR:
        entry_block = get_entry_block(entry_block['header']['prevkeymr'])
        blocks.append(entry_block)

    return blocks

def get_all_entries(chainid):
    blocks = get_all_blocks(chainid)

    entries = []
    for block in blocks:
        for entry in block['entrylist']:
            entries.append(get_entry(entry['entryhash']))

    return entries

def _hexencode(_string):
    return codecs.encode(bytes(_string.encode()), encoding='hex').decode()

def _hexdecode(b64_string):
    return codecs.decode(b64_string, "hex").decode('utf-8')
