# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from math import floor
limit = 2*(10**6)
sievebound = (limit-1)/2
crosslimit = (int(floor(limit**0.5))-1)/2
sieve = [False for x in xrange(0, sievebound+1)]
for i in xrange(1,crosslimit+1):
    if not sieve[i]:
        for j in xrange(2*i*(i+1),sievebound+1,(2*i)+1):
            sieve[j] = True
sum = 2
for i in xrange(1,sievebound+1):
    if not sieve[i]:
        sum += 2*i+1

print sum