# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

from math import floor
limit = 1000
triangles = [0 for x in xrange(limit)]
for cathetus1 in xrange(3,(limit-3)/3):
    for cathetus2 in xrange(cathetus1+1,(limit-cathetus1-1)/2):
        hypotenuse = (cathetus1**2 + cathetus2**2)**0.5
        if floor(hypotenuse) == hypotenuse:
            circumference = int(cathetus1+cathetus2+hypotenuse)
            if circumference > 1000:
                break
            triangles[circumference-1] += 1
            # print("{%d,%d,%d}" %(cathetus1, cathetus2, hypotenuse))
max = 0
for i in xrange(limit):
    if triangles[i] > max:
        max = triangles[i]
        place = i
print ("triangles: %d\ncircumference: %d " %(triangles[place], place+1))
# 840