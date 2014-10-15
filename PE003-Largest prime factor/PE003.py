# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def is_prime(number):
    if number <= 3:
        if number <= 1:
            return False
        return True
    if not number % 2 or not number % 3:
        return False
    for i in range(5, int(number ** 0.5) + 1, 6):   
        if not number % i or not number % (i + 2):
            return False
    return True

num = 600851475143
max_factor = 0
while num > 1:
    for i in xrange(2, num+1):
        if num % i == 0:
            if is_prime(i):
                if i > max_factor:
                    max_factor = i
            num = num / i
            break
print max_factor
# 6857         