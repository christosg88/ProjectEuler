# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

limit = 10001
list_of_primes = [2]
count = 1
number = 3
flag = True
while flag:
    is_prime = True
    root = number**0.5
    for prime in list_of_primes:
        if number % prime == 0:
            is_prime = False
            break
        if prime > root:
            break
    
    if is_prime:
        list_of_primes.append(number)
        count += 1

    if count == limit:
        flag = False
        break
    number += 2

print list_of_primes[limit-1]
# 104743