# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

def FreqOfDigits(number):
    digits = [0 for x in xrange(10)]
    for digit in list(str(number)):
        digits[int(digit)] += 1
    return digits

n = 1
flag = True
while flag:
    k = 2
    while k <= 6:
        if FreqOfDigits(n) != FreqOfDigits(k*n):
            break
        k += 1
    if k == 7:
        print n
        break
    n += 1
# 142857       