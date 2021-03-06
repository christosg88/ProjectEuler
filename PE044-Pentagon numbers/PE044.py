# Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten
# pentagonal numbers are:
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
# 70 - 22 = 48, is not pentagonal.
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
# difference are pentagonal and D = |Pk - Pj| is minimized; what is the value
# of D?

n = 0
flag = True
while flag:
    n += 1
    i = -1
    while abs(i) < n:
        D = abs(((3*(i**2)) + (6*n*i) - i) / 2)
        x = (1 + ((1 + (24*D))**0.5)) / 6.0
        if x == int(x):
            S = ((6*(n**2)) + (3*(i**2)) + (6*n*i) - (2*n) - i) / 2
            y = (1 + ((1 + (24*S))**0.5)) / 6.0
            if y == int(y):
                print ("D = %d\n S = %d\n n = %d" %(D, S, n))
                flag = False
                break
        i -= 1
# 5482660