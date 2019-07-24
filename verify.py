import ecdsa

# put the hex of your public key in the line below
vk_string="324c3af2029a6b5e071c93b427755a44a10033691e2a4ff4b140ad4d74cdee5241ec5dd9a3b510c46de009aeee9ac7bdc82ff33f61d6bd78601321691419ffbd"
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk_string),ecdsa.SECP256k1)

message = b'Hello world'

# put your signature for Hello World in the line below
sig_hex = "99799954427902f68cb535e28f3d81e4771dddc7b25edbe4c305d32e48afb58a6c1b8767b57241160efe8a51bcea83eeba005f2e751cf069406f4f053720c78b"
sig = bytes.fromhex(sig_hex)

print("Checking signature")
print("Message: "+str(message))

print("Signature: "+sig_hex)
print("Public key: "+vk_string)
try:
    vk.verify(sig, message)# True
    print('Verification passed')
except ecdsa.keys.BadSignatureError:
    print('Verification failed')