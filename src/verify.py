from ed25519 import BadSignatureError
import json
from game import sign, verify 

# create entry content w/ valid payload
data = sign(player='X', move='11')

# does not raise an exception because event matches sig
verify(**data)
print(data)
print("verified sig")

print('------------------')

try:
    # Try to verify an event w/o the proper payload
    bad_data = dict(event=json.dumps({'player': 'X'}), sig=data['sig'])
    print(bad_data)
    verify(**bad_data)
except BadSignatureError:
    print("Successfully caught bad sig")

