# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital. The product 7254 is unusual, as the identity, 39 * 186
# = 7254, containing multiplicand, multiplier, and product is 1 through 9
# pandigital. Find the sum of all products whose
# multiplicand/multiplier/product identity can be written as a 1 through 9
# pandigital. HINT: Some products can be obtained in more than one way so be
# sure to only include it once in your sum.

products = []
digits = [0 for i in xrange(10)]
for x in xrange(1,2000):
    for y in xrange(1,2000):
        flag = True
        a = x
        b = y
        for z in xrange(0,10):
            digits[z] = 0
        product = x * y
        temp = product
        while a != 0:
            digits[a % 10] += 1
            a = a / 10
        while b != 0:
            digits[b % 10] += 1
            b = b / 10
        while temp != 0:
            digits[temp % 10] += 1
            temp = temp / 10
        if digits[0] != 0:
            continue
        for z in xrange(1,10):
            if digits[z] != 1:
                flag = False
                break
        if flag:
            for z in products:
                if z == product:
                    flag = False
                    break
        if flag:
            # print x, y, product
            products.append(product)
print sum(products)
# 45228