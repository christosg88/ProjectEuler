# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.

power = 5
total = 0
for i in xrange(2,power*(10**power)):
    num = i
    sum = 0
    while num != 0:
        sum += (num % 10)**power
        num = num / 10
    if sum == i:
        total += i
print total
# 443839