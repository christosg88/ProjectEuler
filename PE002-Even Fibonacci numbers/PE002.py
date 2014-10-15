limit = 4000000
first = 1
second = 1
next = first + second
sum = 0
while next < limit:
    if next % 2 == 0:
        sum += next
    first = second
    second = next
    next = first + second
print sum
# 4613732