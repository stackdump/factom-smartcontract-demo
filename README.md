Example Repo

This repo demonstrates how to create smart contracts on Factom Blockchain.

### Status

Some intended features are not implemented - see [TODO.md](TODO.md)

### Pre-Reqs

* Should have already installed Factomd, factom-wallet and factom-cli.
* Should have python 2/3 & pip installed

### Setup

Install needed python libraries

```
pip install -r requirements.txt
```

Start factomd & factom-wallet

```
./start.sh
```
If walletd started sucessfully you should be able to see the control panel
[http://127.0.0.1:8090](http://127.0.0.1:8090) in a browser.


If walletd started sucessfully you should be able to list some addressess
that were automatically imported by the run.sh script
```
user@dev:~/smartcontracts$ factom-cli listaddresses
FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q 20000
EC3Hu1W7uMHf7CtSva1cMyr5rXKsu7rVqQtkJCDHqEV9dgh5FjAj 0
```

Buy some entry credits using the demo account.

```
user@dev:~$ factom-cli buyec FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q  EC3Hu1W7uMHf7CtSva1cMyr5rXKsu7rVqQtkJCDHqEV9dgh5FjAj  500
TxID: e320e35e40fd66af8faa78e34005dfebd2f9c13080eb87665f59ede0d2af9706
Status: TransactionACK
```

Listing the addresses again shows that we have converted factoids to entry credits.
```
user@dev:~/smartcontracts$ factom-cli listaddresses
FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q 19999.99488
EC3Hu1W7uMHf7CtSva1cMyr5rXKsu7rVqQtkJCDHqEV9dgh5FjAj 500
```

### Run Examples

#### Generate identity keys

Create key files used to sign & valid entries being pushed into a factom chain.

NOTE: in this example we pretend to be both PlayerX and PlayerO
in a more realistic environment each user would only have access to their own secret key
and the public key of the other user.

```
 user@dev:~/smartcontracts$ python src/gen_keys.py
 => generating new player keys
wrote playerX-secret-key
playerX public key is b'f0ebc6091e5d6d3772328651b4fc3efcf8bc7a4aec6589a5857494f39ab00417'
wrote playerO-secret-key
playerO public key is b'a6d574fadf8f2a8085a4c3096878a82bce49d76a84b0d50ef626bee618e26cba'
```

#### Simulate a game of tic-tac-toe

Creates a valid stream of event entries on a factom chain

```
user@dev:~/smartcontracts$ python src/play.py
=> created chain d29343de48e15eada270c8e066468c139712d0bf599ed65c1e2f540c820b7a63
------------------
=> move({"event": "{\"player\": \"X\", \"move\": \"11\", \"seq\": 1}", "sig": "c42590f6a98202bbb1a027705978d62acf5482d52587728728895df91d9a8e92ab2f60a7a2386a997d1bb59c5141a407f9a433c818b8ce2f47cc7b78f8fbdf04"})

{'message': 'Entry Reveal Success', 'entryhash': 'afe695277d94677d767683befabb73a6f079fe0591dbca5c738d34b6913f392c', 'chainid': 'd29343de48e15eada270c8e066468c139712d0bf599ed65c1e2f540c820b7a63'}
------------------
=> move({"event": "{\"player\": \"O\", \"move\": \"02\", \"seq\": 2}", "sig": "5c4c33c867efcc38132d60f8dad181d00c295c8341655bfd389aff4065f9c572d3ffb5155ccf8cbdca6850df1e51eb032068b75a01a0553db7e3678eb165b707"})

{'message': 'Entry Reveal Success', 'entryhash': '90162e60ddf8d2ea95f9fff4fec23b22f9d59d6708a25b2e6ee228354b6be54b', 'chainid': 'd29343de48e15eada270c8e066468c139712d0bf599ed65c1e2f540c820b7a63'}
------------------
=> move({"event": "{\"player\": \"X\", \"move\": \"22\", \"seq\": 3}", "sig": "8632b0cd2088c56061301ff8e304fdcd8db09b356628714e4e350b45289922f84c3c72dd47cf0b7d746cd1f95a722f5b9973a9aadb98b34674cab6fb3d59720f"})

{'message': 'Entry Reveal Success', 'entryhash': '497d5ae7d53ff08ec26678bfaee0fad14da3b0ed0a95d91401111a31a1f40894', 'chainid': 'd29343de48e15eada270c8e066468c139712d0bf599ed65c1e2f540c820b7a63'}
------------------
=> move({"event": "{\"player\": \"O\", \"move\": \"00\", \"seq\": 4}", "sig": "73a4af76a01e522e7f42b92ccdbaeef62a5f5f38b9f7137f1ca45a1be769b188f48f0c776d08e7482d2d2148f0462c5760c547a13c7893ceae7d5a21ba0a2303"})

{'message': 'Entry Reveal Success', 'entryhash': 'bc2bd7313c0b8b00416d6e4c5b0fcfc0c3199b093b1373bd784fac5914c4bc56', 'chainid': 'd29343de48e15eada270c8e066468c139712d0bf599ed65c1e2f540c820b7a63'}
------------------
=> move({"event": "{\"player\": \"X\", \"move\": \"01\", \"seq\": 5}", "sig": "5466db0501d25457ef0d66d262580797085f7903ec5a9850ef61a00daffa3a2c51627fad617a25f948aac4ccbbe88a78f0461f97f9f37b345c71642ea972840a"})

{'message': 'Entry Reveal Success', 'entryhash': '09a07bd2cb6bd07823091ba3a417763e4c01b773650d88b34376852fd13587ea', 'chainid': 'd29343de48e15eada270c8e066468c139712d0bf599ed65c1e2f540c820b7a63'}
------------------
=> move({"event": "{\"player\": \"O\", \"move\": \"10\", \"seq\": 6}", "sig": "d82ca4ea762c4d1fd43ef1a0b713626e4aac59bb1e0f59eb6347852bb54874679d8e51c96b8ac2035569e704dfec265652e40fdabda064b86d93ce2333d9fe04"})

{'message': 'Entry Reveal Success', 'entryhash': '041570219b486244102660f7188a3a8e81c4b5635c7be716edcdd826057a54ee', 'chainid': 'd29343de48e15eada270c8e066468c139712d0bf599ed65c1e2f540c820b7a63'}
------------------
=> move({"event": "{\"player\": \"X\", \"move\": \"21\", \"seq\": 7}", "sig": "d9c31c5a6f3c603f20b906ba41a37db766c265f564d1715a7ae5cf2c381e44e250da10741ca74cd8649e69fe9809cb008f75c80754037a7450c8c08491f40809"})

{'message': 'Entry Reveal Success', 'entryhash': '99c44e7fae4ea24f9aa50a0060d558a7a400deba9424dfbb44a9352bf0ee185f', 'chainid': 'd29343de48e15eada270c8e066468c139712d0bf599ed65c1e2f540c820b7a63'}
------------------
=> Win({"event": "{\"player\": \"X\", \"result\": \"Win\", \"seq\": 8}", "sig": "0a932e53029209453775b6600818b96d4018da82c7a12847459d562de44073d75bd3593cf204c23d8413791a3012b024aa6a3d71233699a91769dd1eda4fd401"})

{'message': 'Entry Reveal Success', 'entryhash': '6b72f570bd8be34567b57d921d78654d59593b2da9a148d7d9623243c6e49dcb', 'chainid': 'd29343de48e15eada270c8e066468c139712d0bf599ed65c1e2f540c820b7a63'}
------------------
Review blochain entries:
http://127.0.0.1:8090/search?input=d29343de48e15eada270c8e066468c139712d0bf599ed65c1e2f540c820b7a63&type=chainhead
```

#### test signature validation

NOTE: this is a simple example of signature validation w/o involving a blockchain

```
user@dev:~/smartcontracts$ python src/verify.py
{'event': '{"player": "X", "move": "11"}', 'sig': 'd77b2b1cdd38ac7a53680580d2679beeff4b6df96796b53dba7e230d757762d3cae11f604bc913ed124ebafebffdfdc66ce956736ac7a1301a32a20d75954304'}
verified sig
------------------
{'event': '{"player": "X"}', 'sig': 'd77b2b1cdd38ac7a53680580d2679beeff4b6df96796b53dba7e230d757762d3cae11f604bc913ed124ebafebffdfdc66ce956736ac7a1301a32a20d75954304'}
Successfully caught bad sig
```

#### Audit event stream for valid gameplay

Run the audit program passing in the chainid as an arg.

```
user@dev:~/smartcontracts$ python src/audit.py
['./src/audit.py', '2d0fefc826d4a6e8c4bf8db187980bd5e743fc161ede0aa20cc75a577afa98d4']
GameInfo:
 {'name': 'XO-1536763959.0636046', 'audit_program': '028b635a83df0bd54707fecd9d818edba5049b5a', 'PlayerX': 'pubkey', 'PlayerO': 'pubkey'}
Moves:
{'player': 'X', 'move': '11', 'seq': 1}
{'player': 'O', 'move': '02', 'seq': 2}
{'player': 'X', 'move': '22', 'seq': 3}
{'player': 'O', 'move': '00', 'seq': 4}
{'player': 'X', 'move': '01', 'seq': 5}
{'player': 'O', 'move': '10', 'seq': 6}
{'player': 'X', 'move': '21', 'seq': 7}
Final:
 {'player': 'X', 'result': 'Win', 'seq': 8}
```

### Shutdown

Shutdown factom services w/ this shell script

```
./stop.sh
```

### Tips/Tricks

On linux you can spy on traffic going to/from factomd
using https://linux.die.net/man/1/tcpflow

```
sudo tcpflow -c -i lo tcp port 8088
```

See a full capture of traffic from this demo  in [traffic_capture_full_demo.txt](./traffic_capture_full_demo.txt)

Here's a list of each api method being invoked - separated into groups of operations [api-summary.txt](api-summary.txt)
