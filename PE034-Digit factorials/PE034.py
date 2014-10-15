# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of
# their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        product = 1
        for x in xrange(2,n+1):
            product *= x
        return product

total = 0
for i in xrange(3,50000):
    m_sum = 0
    num = i
    while num != 0:
        m_sum += fact(num % 10)
        num = num / 10
    if m_sum == i:
        total += i
print total
# 40730