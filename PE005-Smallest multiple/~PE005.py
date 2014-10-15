# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# see https://projecteuler.net/overview=005
def is_prime(number):
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

from math import floor
from math import log
# List of primes from 2 to k
k = 20
list_of_primes = []
for x in xrange(2,k+1):
    if is_prime(x):
        list_of_primes.append(x)
exponents = [1 for x in xrange(0,len(list_of_primes))]
N = 1
limit = k**0.5
flag = True
index = 0
while list_of_primes[index] <= k:
    exponents[index] = 1
    if flag:
        if list_of_primes[index] <= limit:
            exponents[index] = int(floor(log(k) / log(list_of_primes[index])))
        else:
            flag = False
    N *= (list_of_primes[index] ** exponents[index])
    index += 1
    if index >= len(list_of_primes):
        break
print N
# 232792560