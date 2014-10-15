# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime
# at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
# left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left
# to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def is_prime(num):
    if num <= 1 or (num % 2 == 0 and num != 2):
        return False
    else:
        for i in xrange(2,int(num**0.5)+1):
            if num % i == 0:
                return False
    return True

unfinished = True
n = 10
count = 0
m_sum = 0
while unfinished:
    if is_prime(n):
        flag = True
        digits = str(n)
        length = len(digits)
        for x in xrange(length):
            temp1 = int("".join(digits[0:length-x]))
            temp2 = int("".join(digits[x:length]))
            if (not is_prime(temp1)):
                flag = False
                break
            if (not is_prime(temp2)):
                flag = False
                break
        if flag:
            m_sum += n
            count += 1
            # print n
    n += 1
    if count == 11:
        unfinished = False
print m_sum
# 748317