# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?

from math import log10
base = 2
power = 1000

number = [0 for i in xrange(1+int(power*log10(base)))]
length = len(number)
number[length-1] = base
for i in xrange(power-1):
    for j in xrange(length):
        number[j] *= base
        if number[j] > 9:
            number[j-1] += 1
            number[j] %= 10
digit_sum = 0
for digit in number:
    digit_sum += digit
print digit_sum
# 1366