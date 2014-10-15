# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:
# (triangle.txt)
# NOTE: As there are only 16384 routes, it is possible to solve this problem by
# trying every route. However, Problem 67, is the same challenge with a triangle
# containing one-hundred rows; it cannot be solved by brute force, and requires
# a clever method! ;o)

rows = 15
with open("triangle.txt", "r") as triangle:
    numbers = [[0 for y in xrange(x+1)] for x in xrange(rows)]
    for i in xrange(rows):
        line = triangle.readline()
        str_numbers = line.split()
        for j in xrange(i+1):
            numbers[i][j] = int(str_numbers[j])

    for i in xrange(rows-1, 0, -1):
        for j in xrange(i):
            numbers[i-1][j] += max(numbers[i][j], numbers[i][j+1])
    print numbers[0][0]
# 1074