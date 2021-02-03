import timeit
import hashlib

def hsha1(t):   #hash in sha1 format
    return hashlib.sha1(t.encode()).hexdigest()

fr = open('text.txt', 'r')
Lines = fr.readlines()
fr.close()
count = 0

starttime = timeit.default_timer()
print("The start time is :",starttime)
for l in Lines:
    hsha1(l)
    count = count + 1
Time = timeit.default_timer() - starttime
print("The time difference is :", Time)
print("Number of text hashed is " + str(count))
print("Avg time per hash = " + str(Time/count) + ' seconds')