from math import floor
def sieve(limit, start = 0):
    # sieve(maxPrime, [minPrime])
    sievebound = (limit-1)/2
    crosslimit = (int(floor(limit**0.5))-1)/2
    sieve = [False for x in xrange(0, sievebound+1)]
    for i in xrange(1,crosslimit+1):
        if not sieve[i]:
            for j in xrange(2*i*(i+1),sievebound+1,(2*i)+1):
                sieve[j] = True
    final = [2]
    for i in xrange(1,sievebound+1):
        if not sieve[i]:
            final.append(2*i+1)
    k = 0
    while final[k] < start:
        k += 1
    return final[k:]