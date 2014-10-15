# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from fractions import gcd
s = 100000
s2 = s / 2
mlimit = int(s2**0.5) - 1
for m in xrange(2,mlimit+1):
    if s2 % m == 0:
        sm = s2 / m
        while sm % 2 == 0:
            sm /= 2
        if m % 2 == 1:
            k = m+2
        else:
            k = m+1
        while k < 2*m and k <= sm:
            if (sm % k == 0) and gcd(k,m) == 1:
                d = s2 / (k*m)
                n = k-m
                a = d * (m**2 - n**2)
                b = 2 * d * m * n
                c = d * (m**2 + n**2)
                print a*b*c
            k += 2