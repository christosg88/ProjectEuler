# Starting in the top left corner of a 2*2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20*20 grid?

N = 20

triangle = [[1 for j in xrange(i+1)] for i in xrange((2 * N) + 1)]

for i in xrange(2*N+1):
    for j in xrange(1,i):
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

print triangle[2*N][N]
# 137846528820