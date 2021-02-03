import timeit
import hashlib

def hsha1(t):   #hash in sha1 format
    return hashlib.sha1(t.encode()).hexdigest()

starttime = timeit.default_timer()
print("The start time is :",starttime)
hsha1('a')
print("The time difference is :", timeit.default_timer() - starttime)