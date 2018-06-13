#!/usr/bin/env python3
import os
class OutPoint(object):


    """docstring for OutPoint"""
    def __init__(self, random=os.urandom):
        self.txid=random(32)
        self.n=random(4)




class TxIn(object):

    """docstring for TxIn"""
    def __init__(self, random=os.urandom):
        self.prevout=OutPoint(random)
        self.scriptSig=b'\x00\x51'*(ord(random(1)) % 3)
        self.nSequence=random(4)

class TxOut(object):

    """docstring for TxIn"""
    def __init__(self, random=os.urandom):
        self.nValue=random(8)
        self.scriptPubKey=b'\x00\x51'*(ord(random(1)) % 3)




class Transaction(object):
    # header=b''
    # nVersionGroupId=b''
    # tx_in=[]
    # tx_out=[]
    # lock_time=0
    # nExpiryHeight=0
    # valueBalance=0
    # vShieldedSpend=[]
    # vShieldedOutput=[]
    # vJoinSplit=[]
    # joinSplitPubKey=b''
    # joinSplitSig=b''
    # bindingSig=b''


    # @staticmethod
    # def rand(random=os.urandom):
    #     header=random(4)
    #     nVersionGroupId=random(4)
    #     for i in xrange(0,ord(random(1)) % 3):
    #         tx_in.append(TxIn.rand(random))
    #     lock_time=random(4)
    #     nExpiryHeight=random(4)
    #     valueBalance=random(8)
    #     joinSplitPubKey=random(32)



    """docstring for Transaction"""
    def __init__(self, random=os.random):
        header=random(4)
        nVersionGroupId=random(4)
        for i in xrange(0,ord(random(1)) % 3):
            tx_in.append(TxIn(random))
        for i in xrange(0,ord(random(1)) % 3):
            tx_out.append(TxOut(random))
        lock_time=random(4)
        nExpiryHeight=random(4)
        valueBalance=random(8)
        joinSplitPubKey=random(32)

        