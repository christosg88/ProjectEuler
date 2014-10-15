# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

sum = 0
for x in xrange(1,1001):
    sum += x**x
str_sum = str(sum)
print str_sum[len(str_sum)-10:]
# 9110846700