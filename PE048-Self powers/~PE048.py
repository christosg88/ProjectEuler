# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

def normalize(inNumber):
    for x in xrange(len(inNumber)-1,0,-1):
        inNumber[x-1] += inNumber[x] / 10
        inNumber[x] = inNumber[x] % 10
    inNumber[0] = inNumber[0] % 10
    return inNumber

sum = [0 for x in xrange(10)]
for x in xrange(1,1001):
    number = [0 for y in xrange(10)]
    number[9] = x
    for y in xrange(x-1):
        for k in xrange(10):
            number[k] *= x
        normalize(number)
    for y in xrange(10):
        sum[y] += number[y]
    normalize(sum)
print int(''.join(map(str,sum)))
# 9110846700