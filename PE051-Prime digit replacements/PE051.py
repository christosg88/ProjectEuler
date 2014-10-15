# By replacing the 1st digit of the 2-digit number *3, it turns out that six
# of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this
# 5-digit number is the first example having seven primes among the ten
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
# 56773, and 56993. Consequently 56003, being the first member of this family,
# is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.

from datetime import datetime
from math import floor
def sieve(limit, start = 0):
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
    k = 0
    while final[k] < start:
        k += 1
    return final[k:]

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

def FreqOfDigits(number):
    digits = [0 for x in xrange(10)]
    for digit in list(str(number)):
        digits[int(digit)] += 1
    return digits

def positions(number, digit):
    places = []
    str_num = list(str(number))
    length = len(str_num)
    for x in xrange(length):
        if int(str_num[x]) == digit:
            places.append(x)
    return places

start = datetime.now()
primes = sieve(10000000,100)
length = len(primes)
flag = True
max_members = 0
for prime in primes:
    digits = FreqOfDigits(prime)
    for d in xrange(10):
        if digits[d] > 1:
            family = [prime]
            members = 1
            pos = positions(prime, d)
            str_prime = list(str(prime))
            dd = d
            while dd < 9:
                for x in pos:
                    str_prime[x] = str(int(str_prime[x])+1)
                if isPrime(int(''.join(str_prime))):
                    family.append(int(''.join(str_prime)))
                    members += 1
                dd += 1
            if members == 8:
                print family
                flag = False
                break
    if not flag:
        break
print datetime.now() - start
# 121313