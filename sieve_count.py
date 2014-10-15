from math import floor
def sieve_count(number_of_primes):
    sieve = [2]
    count = 1
    number = 3
    while count < number_of_primes:
        limit = int(floor(number**0.5))
        for prime in sieve:
            if number % prime == 0:
                break
            if prime > limit:
                sieve.append(number)
                count += 1
                print count, number
                break
        number += 2
    return sieve

sieve_count(10**9)