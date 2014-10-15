# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

limit = 2*(10**6)
list_of_primes = [2]
number = 3
flag = True
sum = 2
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
        sum += number

    number += 2

    if number >= limit:
        flag = False
        break
print sum