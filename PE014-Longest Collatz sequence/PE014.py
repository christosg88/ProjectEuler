# The following iterative sequence is defined for the set of positive
# integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following
# sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

limit = 10**6
max_terms = 1
for i in xrange(2,limit+1):
    terms = 1
    num = i
    while num != 1:
        terms += 1
        if num % 2 == 1:
            num = (num * 3) + 1
        else:
            num /= 2
    if terms > max_terms:
        max_terms = terms
        max_number = i

print("Number with maximum terms: " + str(max_number))
print("Number of terms: " + str(max_terms))
# 837799