# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from math import floor
def isPrime(number):
    if number == 1:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0:
        return False
    elif number < 9:
        return True
    elif number % 3 == 0:
        return False
    else:
        r = floor(number**0.5)
        f = 5
        while f <= r:
            if number % f == 0:
                return False
            elif number % (f+2) == 0:
                return False
            else:
                f += 6
        return True

limit = 2*(10**6)
sum = 5
n = 5
while n <= limit:
    if isPrime(n):
        sum += n
    n += 2
    if (n <= limit) and isPrime(n):
        sum += n
    n += 4
print sum