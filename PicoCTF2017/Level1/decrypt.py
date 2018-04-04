#!/usr/bin/python
from Crypto.Cipher import AES
from base64 import b64decode

key = b64decode("6v3TyEgjUcQRnWuIhjdTBA==")
ciphertext = b64decode("rW4q3swEuIOEy8RTIp/DCMdNPtdYopSRXKSLYnX9NQe8z+LMsZ6Mx/x8pwGwofdZ")

obj = AES.new(key, AES.MODE_ECB)

plaintext = obj.decrypt(ciphertext)
print "Flag : %s" % plainrtext
