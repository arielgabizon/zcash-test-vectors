#!/usr/bin/env python3
from pyblake2 import blake2b


SIGHASH_ALL = 1,
SIGHASH_NONE = 2,
SIGHASH_SINGLE = 3,
SIGHASH_ANYONECANPAY = 0x80,


# Currently assumes the nHashType is SIGHASHALL
def signature_hash(scriptCode, tx,nIn,nHashType,amount,consensusBranchId):
    hashPrevouts = b'\x00'*32
    hashSequence = b'\x00'*32
    hashOutputs = b'\x00'*32
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
        digest.update(tx.tx_in[nIn].scriptCode)
        digest.update(amount)
        digest.update(nIn)



