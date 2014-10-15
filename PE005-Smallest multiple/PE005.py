# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

flag = True
num = 20
while flag:
    num += 2
    flag = False
    for x in xrange(2,21):
        if num % x != 0:
            flag = True
            break
print num
# 232792560