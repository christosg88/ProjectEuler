# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation, 5C3 = 10.
# In general,
# nCr = n! / r!(n-r)! ,where r <= n, n! = n*(n-1)*...*3*2*1, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
# How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are
# greater than one-million?

from operator import mul
from fractions import Fraction

def nCk(n,k): 
    return int(reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1))

total = 0
for n in xrange(1,101):
    for k in xrange(2,n):
        if nCk(n,k) > 1000000:
            total += 1
print total
# 4075