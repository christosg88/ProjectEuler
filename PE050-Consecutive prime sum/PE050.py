# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below
# one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a
# prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

from math import floor
from datetime import datetime
def sieve(limit):
    sievebound = (limit-1)/2
    crosslimit = (int(floor(limit**0.5))-1)/2
    sieve = [False for x in xrange(0, sievebound+1)]
    for i in xrange(1,crosslimit+1):
        if not sieve[i]:
            for j in xrange(2*i*(i+1),sievebound+1,(2*i)+1):
                sieve[j] = True
    final = [2]
    for i in xrange(1,sievebound+1):
        if not sieve[i]:
            final.append(2*i+1)
    return final

def isPrime(number):
    if number <= 3:
        if number <= 1:
            return False
        return True
    if not number % 2 or not number % 3:
        return False
    for i in range(5, int(number ** 0.5) + 1, 6):   
        if not number % i or not number % (i + 2):
            return False
    return True

start = datetime.now()
limit = 1000000
test_primes = sieve(limit)
primes = []
p_sum = 0
x = 0
while p_sum <= limit:
    primes.append(test_primes[x])
    p_sum += test_primes[x]
    x += 1
length = len(primes)
longest = length
flag = True
while longest > 0 and flag:
    i = 0
    while i + longest <= length:
        p_sum = sum(primes[i:i+longest+1])
        if p_sum < limit:
            if isPrime(p_sum):
                print sum(primes[i:i+longest+1])
                flag = False
                break
        i += 1
    longest -= 1
print datetime.now() - start
# 997651