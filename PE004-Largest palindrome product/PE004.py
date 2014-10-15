# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

number_of_digits = 3
mul = 0

for first in xrange((10**number_of_digits)-1, (10**(number_of_digits-1))-1, -1):
    for second in xrange((10**number_of_digits)-1, (10**(number_of_digits-1))-1, -1):
        flag = True
        c_mul = str(first * second)
        length = len(c_mul)
        for x in xrange(0,length/2):
            if c_mul[x] != c_mul[length - (x+1)]:
                flag = False
                break
        if (first * second > mul) and (flag == True):
            mul = first * second
print mul
# 906609