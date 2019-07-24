import hashlib
import json
import time 

"""
#### FUNCTION LIST   ####
"""

#pads strings of hexvalues to have length 64 for easier readability
#taken from https://codereview.stackexchange.com/questions/67611/padding-a-hexadecimal-string-with-zeros
def padhexa(s):                         
    return '0x' + s[2:].zfill(64)

def verifyValidBlock():
    # Simplified conversion of block header into bytes:
    block_serialised = json.dumps(example_block_header, sort_keys=True).encode()

    # Double SHA256 hashing of the serialised block
    block_hash=hashlib.sha256(hashlib.sha256(block_serialised).digest()).hexdigest()
    
    return (currentTarget > int(block_hash,16) )

def mineValidBlock():
    #initialise
    print('Mining Valid Block...')
    print('')
    example_block_header['nonce'] = 0       
    hashes = 0
    startTime = time.time()
    
    #start hashing
    while(True):
        hashes += 1
        if(verifyValidBlock() ):
            finishTime = time.time()
            timeTaken = finishTime - startTime
            print("Hashes Performed: " + str((hashes)) )
            print("Time Taken (seconds): " + str(timeTaken) )
            print("Time per Hash: " + str(timeTaken/hashes))
            print('')
            block_serialised = json.dumps(example_block_header, sort_keys=True).encode()
            block_hash=hashlib.sha256(hashlib.sha256(block_serialised).digest()).hexdigest()
            print('Hash with nonce ' + str(example_block_header['nonce'])+': '+ padhexa(str(hex(int(block_hash, 16)))) )
            print('Block is valid')
            print('')
            break
        else:
           example_block_header['nonce'] += 1 

"""
####  EXECUTED CODE  ####
"""


# An example block header - do not change any fields except nonce and coinbase_addr
example_block_header = {'height': 1478503,
                        'prev_block': '0000000000000da6cff8a34298ddb42e80204669367b781c87c88cf00787fcf6',
                        'total': 38982714093,
                        'fees': 36351,
                        'size': 484,
                        'ver': 536870912,
                        'time': 1550603039.882228,
                        'bits': 437239872,
                        'nonce': 287772,                     #You may change this field of the block
                        'coinbase_addr': 'gvch48',     #You should change this field of the block to your studentID
                        'n_tx': 2,
                        'mrkl_root': '69224771b7a2ed554b28857ed85a94b088dc3d89b53c2127bfc5c16ff49da229',
                        'txids': ['3f9dfc50198cf9c2b0328cd1452513e3953693708417440cd921ae18616f0bfc', '3352ead356030b335af000ed4e9030d487bf943089fc0912635f2bb020261e7f'],
                        'depth': 0}

original_target = 0x00000000ffff0000000000000000000000000000000000000000000000000000
difficulty = 0.001
# target and expectedNumHashes computation from https://en.bitcoin.it/wiki/Difficulty
currentTarget = int((0xffff * 2**208)/difficulty)
expectedNumHashes = int(difficulty * 2**48 / 0xffff)

print("Current Difficulty: " + str(difficulty) )
print("Original Target: " + padhexa(str(hex(original_target))) )
print("Current Target: " + padhexa(str(hex(currentTarget))) )
print("Expected Number of hashes required: " + str(expectedNumHashes))
print('')

mineValidBlock()

print("Hashes performed on my PC: 287773")
print("Time taken on my PC (seconds): 6.2888710498809814")
timePerHash = 6.2888710498809814 / 287773
print("Time per hash on my PC (seconds): " + str(timePerHash) )
print('')

ExpectedNumHashesAtOne = int(1 * 2**48 / 0xffff)
ExpectedTimeAtOne = timePerHash * ExpectedNumHashesAtOne
print("Expected Number of Hashes at Difficulty 1: " + str(ExpectedNumHashesAtOne) )
print("Expected Time to Mine on my PC (seconds): " + str(ExpectedTimeAtOne))
print("Expected Time to Mine on my PC (hours): " + str(ExpectedTimeAtOne/(60*60) ) )
print('')

ExpectedNumHashesAtMax = int(7454968648263 * 2**48 / 0xffff)
ExpectedTimeAtMax = timePerHash * ExpectedNumHashesAtMax
print("Expected Number of Hashes at Difficulty 7,454,968,648,263: " + str(ExpectedNumHashesAtMax) )
print("Expected Time to Mine on my PC (seconds): " + str(ExpectedTimeAtMax))
print("Expected Time to Mine on my PC (years): " + str(ExpectedTimeAtMax / (60*60*24*365.25) ) )
print('')



