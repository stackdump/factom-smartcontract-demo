"""
Run this script to create new signing keys
The generated files are used to sign and verify entries written to the factom blockchain.
"""
import ed25519

def generate_key(prefix):
    """ generate a private key """
    signing_key, verifying_key = ed25519.create_keypair()
    filename = prefix + "-secret-key"
    open(filename, "wb").write(signing_key.to_bytes())
    print('wrote ' + filename)
    vkey_hex = verifying_key.to_ascii(encoding="hex")
    print(prefix + " public key is", vkey_hex)

print('=> generating new player keys')
generate_key('playerX')
generate_key('playerO')
