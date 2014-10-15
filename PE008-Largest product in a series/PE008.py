# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9 * 9 * 8 * 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the
# greatest product. What is the value of this product?

def product_fun(n):
    pro = 1
    for x in xrange(0,len(n)):
        pro *= n[x]
    return pro

lines = 20
line_length = 50
max_product = 0
MAX = 13
num = []

with open("number.txt", "r") as number:
    for x in xrange(0,20):
        line = (number.readline()).strip("\n")
        for char in line:
            num.append(int(char))
    for y in xrange(0,(line_length*lines)-MAX+1):
        product = product_fun(num[0+y:MAX+y])
        if product > max_product:
            max_product = product
print max_product
# 23514624000