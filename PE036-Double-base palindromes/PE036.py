# The decimal number, 585 = 10010010012 (binary), is palindromic in both
# bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include
# (leading zeros.)

def is_palindromic(num):
    digits = []
    flag = True
    while num != 0:
        digits.insert(0, num % 10)
        num = num / 10
    length = len(digits)
    for index in xrange(length / 2):
        if digits[index] != digits[length - 1 - index]:
            flag = False
            break
    return flag

m_sum = 0
for x in xrange(1,1000000):
    if is_palindromic(x):
        if is_palindromic(int("".join(bin(x)[2:]))):
            m_sum += x
            # print x
            # print bin(x)[2:]
print m_sum
# 872187