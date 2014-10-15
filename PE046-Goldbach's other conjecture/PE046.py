# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.
# 9 = 7 + 2*1^2
# 15 = 7 + 2*2^2
# 21 = 3 + 2*3^2
# 25 = 7 + 2*3^2
# 27 = 19 + 2*2^2
# 33 = 31 + 2*1^2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a
# prime and twice a square?

def isPrime(number):
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

def findNextPrime():
    n = primes[len(primes)-1]
    while True:
        n += 1
        if isPrime(n):
            primes.append(n)
            return

primes = [2]
i = 1
flag = True
while flag:
    i += 2
    if not isPrime(i):
        isGoldbach = False
        while primes[len(primes)-1] + 2 < i:
            findNextPrime()
        for p in primes:
            n = 1
            sum = p + 2*(n**2)
            while sum < i:
                n += 1
                sum = p + 2*(n**2)
            if sum == i:
                isGoldbach = True
                break
        if not isGoldbach:
            print i
            flag = False
# 5777