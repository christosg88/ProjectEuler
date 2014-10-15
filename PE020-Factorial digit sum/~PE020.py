# n! means n * (n - 1) * ... * 3 * 2 * 1
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800
# and the sum of the digits in the number 10!
# is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

from math import log10
number = 100
length = 1+int(number*log10(number))
factorial = [0 for x in xrange(length)]
factorial[length-1] = 1
for curent in xrange(2,number+1):
    for i in xrange(length-1, -1, -1):
        factorial[i] *= curent
    for i in xrange(length-1, -1, -1):
        if factorial[i] > 9:
            factorial[i-1] += factorial[i]/10
            factorial[i] %= 10
print sum(factorial)
# 648