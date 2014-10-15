# A googol (10100) is a massive number: one followed by one-hundred zeros;
# 100100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, a^b, where a, b < 100, what is the
# maximum digital sum?

max = 0
for a in xrange(1,100):
    for b in xrange(1,100):
        t = sum(map(int, list(str(a**b))))
        if t > max:
            max = t
print max
# 972