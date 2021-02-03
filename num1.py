import hashlib
import os
from itertools import product

# r = "hello"
enc_pas = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7"

def hsha1(t):   #hash in sha1 format
    return hashlib.sha1(t.encode()).hexdigest()

# def hmd5(t):   #hash in sha1 format
#     return hashlib.md5(t.encode()).hexdigest()

fr = open('text.txt', 'r')
Lines = fr.readlines()
fr.close()

for line in Lines:
    w = map(''.join, product(*((c.upper(),c.lower()) for c in line)))
    for i in w:
        # print(i.strip())
        if hsha1(i.strip()) == enc_pas:
            print(i.strip())
            exit()
print("nope")