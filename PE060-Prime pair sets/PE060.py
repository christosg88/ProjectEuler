# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
# primes and concatenating them in any order the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of
# these four primes, 792, represents the lowest sum for a set of four primes
# with this property.
# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.

def gen_primes():
    # Sieve of Eratosthenes
    # Code by David Eppstein, UC Irvine, 28 Feb 2002
    # http://code.activestate.com/recipes/117119/
    """ Generate an infinite sequence of prime numbers.
    """
    D = {}
    q = 2  
    while True:
        if q not in D:
            yield q        
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

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

p1 = []
p2 = []
p3 = []
p4 = []

length = 0
n1 = 0
flag = True
for prime in gen_primes():
    p1.append(prime)
    p2.append(prime)
    p3.append(prime)
    p4.append(prime)
    length += 1
    for i in xrange(length):
        if isPrime(int(str(prime)+str(p1[i]))) and \
            isPrime(int(str(p1[i])+str(prime))):
            for j in xrange(i+1, length):
                if isPrime(int(str(prime)+str(p2[j]))) and \
                    isPrime(int(str(p2[j])+str(prime))) and \
                    isPrime(int(str(p1[i])+str(p2[j]))) and \
                    isPrime(int(str(p2[j])+str(p1[i]))):
                    for k in xrange(j+1, length):
                        if isPrime(int(str(prime)+str(p3[k]))) and \
                            isPrime(int(str(p3[k])+str(prime))) and \
                            isPrime(int(str(p1[i])+str(p3[k]))) and \
                            isPrime(int(str(p3[k])+str(p1[i]))) and \
                            isPrime(int(str(p2[j])+str(p3[k]))) and \
                            isPrime(int(str(p3[k])+str(p2[j]))):
                            for z in xrange(k+1,length):
                                if isPrime(int(str(prime)+str(p4[z]))) and \
                                    isPrime(int(str(p4[z])+str(prime))) and \
                                    isPrime(int(str(p1[i])+str(p4[z]))) and \
                                    isPrime(int(str(p4[z])+str(p1[i]))) and \
                                    isPrime(int(str(p2[j])+str(p4[z]))) and \
                                    isPrime(int(str(p4[z])+str(p2[j]))) and \
                                    isPrime(int(str(p3[k])+str(p4[z]))) and \
                                    isPrime(int(str(p4[z])+str(p3[k]))):
                                    print prime, p1[i], p2[j], p3[k], p4[z]
                                    flag = False
                                    break
                        if not flag:
                            break
                if not flag:
                    break
        if not flag:
            break
    if not flag:
        break
# 26033