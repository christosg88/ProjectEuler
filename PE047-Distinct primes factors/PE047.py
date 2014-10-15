# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 * 7
# 15 = 3 * 5
# The first three consecutive numbers to have three distinct prime factors
# are:
# 644 = 2^2 * 7 * 23
# 645 = 3 * 5 * 43
# 646 = 2 * 17 * 19.
# Find the first four consecutive integers to have four distinct prime
# factors. What is the first of these numbers?

def primeFactorize(number):
    factors = []
    if isPrime(number):
        listOfPrimes.append(number)
        return factors
    while listOfPrimes[len(listOfPrimes)-1] <= number**0.5:
        findNextPrime()

    for prime in listOfPrimes:
        if number % prime == 0:
            if prime not in factors:
                factors.append(prime)
            number = number / prime
        if prime > number:
            return factors

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
    n = listOfPrimes[len(listOfPrimes)-1]
    while True:
        n += 1
        if isPrime(n):
            listOfPrimes.append(n)
            return

listOfPrimes = [2]
x = 1
consecutiveNumbers = 4
flag = True
p = [[] for x in xrange(consecutiveNumbers)]
while flag:
    flag = False
    x += 1
    p[(x%consecutiveNumbers)-1] = primeFactorize(x)

    while len(p) < consecutiveNumbers:
        p[(x%consecutiveNumbers)-1] = primeFactorize(x)
        x += 1

    for factorList in p:
        if len(factorList) != consecutiveNumbers:
            flag = True
            break
for l in xrange(1,consecutiveNumbers+1):
    print x+l-consecutiveNumbers , primeFactorize(x+l-consecutiveNumbers)

# 134043