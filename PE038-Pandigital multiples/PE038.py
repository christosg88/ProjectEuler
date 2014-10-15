# # Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 * 1 = 192
# 192 * 2 = 384
# 192 * 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We
# will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
# and 5, giving the pandigital, 918273645, which is the concatenated product
# of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

m_max = 0
for x in xrange(1,10**4):
    conc_products = []
    n = 1
    while len(conc_products) < 9:
        conc_products += str(x * n)
        n += 1
    if len(conc_products) > 9:
        continue
    digits = [0 for i in xrange(10)]
    num = int("".join(conc_products))
    while num != 0:
        digits[num % 10] += 1
        num = num / 10
    if digits[0] != 0:
        continue
    flag = True
    for z in xrange(1,10):
        if digits[z] != 1:
            flag = False
            break
    if flag:
        num = int("".join(conc_products))
        if num > m_max:
            m_max = num
print m_max
# 932718654