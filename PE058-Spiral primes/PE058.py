# Starting with 1 and spiraling anticlockwise in the following way, a square
# spiral with side length 7 is formed.
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
# It is interesting to note that the odd squares lie along the bottom right
# diagonal, but what is more interesting is that 8 out of the 13 numbers lying
# along both diagonals are prime; that is, a ratio of 8/13 = 62%.
# If one complete new layer is wrapped around the spiral above, a square
# spiral with side length 9 will be formed. If this process is continued, what
# is the side length of the square spiral for which the ratio of primes along
# both diagonals first falls below 10%?

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

number = 1
step = 2
ratio = 1
primes_found = 0
denominator = 1
while ratio > 0.1:
    for x in xrange(3):
        number += step
        if isPrime(number):
            primes_found += 1
    number += step
    step += 2
    denominator += 4
    ratio = primes_found/float(denominator)
print step-1
# 26241