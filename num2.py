import os
import time
import hashlib
from itertools import product

def hsha1(t):   #hash in sha1 format
    return hashlib.sha1(t.encode("utf-8")).hexdigest()

# def hmd5(t):   #hash in sha1 format
#     return hashlib.md5(t.encode()).hexdigest()

#return list of mix upper and lower case characters.
def ULmix(w):
    return list(set(map(''.join, product(*((c.upper(),c.lower()) for c in w)))))

def filler(word):
    combos = []
    for c in word:
        if c not in options:
            combos.append((c,))
        else:
            ex = [c]
            ex.extend(options[c])
            combos.append(ex)
    return list(set((''.join(o) for o in product(*combos))))

options = {
  'o': ['0'],
  'l': ['1'],
  'i': ['1']}

start = time.time()  #timeit for better performance

fr = open('text.txt', 'r')
Lines = fr.readlines()
fr.close()
#store all data
password_list = [] #password combination list
# hash_list = [] #hash

#read word from text list
for l in Lines:                             # password
    w_list = ULmix(l.strip())               # w_list = ['PASSWORD', 'PASWORd', ....]
    # w.extend(word_mix)
    for w in w_list:                        #!!!the original value is also gone!!!
        f_list = filler(w)                  # f_list = [...,'PASSw0rD',...]
        for f in f_list:
            password_list.append((f.strip(),hsha1(f.strip())))

fw = open('dictionary.txt', 'w')
for i in password_list:
    fw.write(i[0] + "   " + i[1] + '\n')

end = time.time()
 
print('Time: ' + str(end - start) + '\n')
fw.close()
print("Done")