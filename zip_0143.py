#!/usr/bin/env python3
from pyblake2 import blake2b


SIGHASH_ALL = 1,
SIGHASH_NONE = 2,
SIGHASH_SINGLE = 3,
SIGHASH_ANYONECANPAY = 0x80,

def getHashPrevouts(tx):
    digest = blake2b(digest_size=32, person=b'ZcashPrevoutHash')
    for i in xrange(0, tx.tx_in):
        digest.update(tx_in[i].prevout)
    return digest.digest()

def getHashSequence(tx):
    digest = blake2b(digest_size=32, person=b'ZcashSequencHash')
    for i in xrange(0, tx.tx_in):
        digest.update(tx_in[i].nSequence)
    return digest.digest()

def getHashOutputs(tx):
    digest = blake2b(digest_size=32, person=b'ZcashOutputsHash')
    for i in xrange(0, tx.tx_out):
        digest.update(tx_out[i].hash())
    return digest.digest()

def getHashOutputs(tx):
    digest = blake2b(digest_size=32, person=b'ZcashOutputsHash')
    for i in xrange(0, tx.tx_out):
        digest.update(tx_out[i].to_string())
    return digest.digest()



# Currently assumes the nHashType is SIGHASHALL
# and that there are no joinSplits
def signature_hash(scriptCode, tx,nIn,nHashType,amount,consensusBranchId):
    hashPrevouts = getHashOutputs(tx)
    hashSequence = getHashSequence(tx)
    hashOutputs = getHashOutputs(tx)
    hashJoinSplits = b'\x00'*32



    digest = blake2b(digest_size=32, person=b'ZcashSigHash' + consensusBranchId)
    digest.update(tx.header)
    digest.update(tx.versionGroupId)
    digest.update(hashPrevouts)
    digest.update(hashSequence)
    digest.update(hashOutputs)
    digest.update(hashJoinSplits)
    digest.update(tx.lock_time)
    digest.update(tx.nExpiryHeight)
    digest.update(nHashType)
    if nIn is not None:
        digest.update(tx.tx_in[nIn].prevout)
        digest.update(scriptCode)
        digest.update(amount)
        digest.update(nIn)



