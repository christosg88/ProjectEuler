# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
# is correct, is obtained by canceling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and
# denominator.
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

p_numerators = 1
p_denominators = 1
for numerator in xrange(10,51):
    for denominator in xrange(numerator+1, 100):
        if ((numerator % 10) == (denominator / 10)) and (denominator % 10 != 0):
            if ((float(numerator) / denominator) == (float(numerator / 10) / (denominator % 10))):
                # print str(numerator) + "/" + str(denominator)
                p_numerators *= numerator
                p_denominators *= denominator
top = max(p_denominators, p_numerators)
flag = True
n = 2
while flag:
    if ((p_numerators % n == 0) and (p_denominators % n == 0)):
        p_numerators /= n
        p_denominators /= n
        n = 2
        top = max(p_denominators, p_numerators)
        continue
    n += 1
    if n > top:
        flag = False
print str(p_numerators) + "/" + str(p_denominators)
# 1/100