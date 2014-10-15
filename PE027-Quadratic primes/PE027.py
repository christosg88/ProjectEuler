# Euler discovered the remarkable quadratic formula:
# n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive
# values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is
# divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
# divisible by 41. The incredible formula  n^2 - 79n + 1601 was discovered,
# which produces 80 primes for the consecutive values n = 0 to 79. The product
# of the coefficients, -79 and 1601, is -126479.
# Considering quadratics of the form:
# n^2 + an + b, where |a| < 1000 and |b| < 1000
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.

def is_prime(num):
    if num <= 1 or (num % 2 == 0 and num != 2):
        return False
    else:
        for i in xrange(2,int(num**0.5)+1):
            if num % i == 0:
                return False
    return True

def formula(a, b, num):
    return ((num**2) + (a*num) + b)

max_consecutive_primes = 0
for x in xrange(-999,1000):
    for y in xrange(-999,1000):
        consecutive_primes = 0
        n = 0
        while is_prime(formula(x, y, n)):
            consecutive_primes += 1
            n += 1
        if consecutive_primes > max_consecutive_primes:
            max_consecutive_primes = consecutive_primes
            product = x * y
print product
# -59231