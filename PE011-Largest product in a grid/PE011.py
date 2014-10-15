# In the 20*20 grid below, four numbers along a diagonal line
# have been marked in red.
# The product of these numbers is 26 * 63 * 78 * 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20*20 grid?

rows = 20
columns = 20
grid = [[] for x in xrange(rows)]
with open("grid.txt", "r") as grid_file:
    for i in xrange(rows):
        line = (grid_file.readline()).strip("\n")
        grid[i] = line.split(" ")
    
    for i in xrange(rows):
        for j in xrange(columns):
            grid[i][j] = int(grid[i][j])

    max_product = 0
    # checking horizontally
    for i in xrange(rows):
        for j in xrange(columns-3):
            product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            if product > max_product:
                max_product = product

    # checking vertically
    for j in xrange(columns):
        for i in xrange(rows-3):
            product = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            if product > max_product:
                max_product = product

    # checking diagonally
    for i in xrange(rows):
        for j in xrange(columns-3-i):
            # upper diagonals
            product = grid[j][j+i] * grid[j+1][j+i+1] * grid[j+2][j+i+2] * grid[j+3][j+i+3]
            if product > max_product:
                max_product = product
            if i != 0:
                # lower diagonals
                product = grid[j+i][j] * grid[j+i+1][j+1] * grid[j+i+2][j+2] * grid[j+i+3][j+3]
                if product > max_product:
                    max_product = product

    # checking anti-diagonally
    for i in xrange(rows):
        for j in xrange(columns-3-i):
            # upper anti-diagonals
            product = grid[(rows-1)-i-j][j] * grid[(rows-1)-i-j-1][j+1] * grid[(rows-1)-i-j-2][j+2] * grid[(rows-1)-i-j-3][j+3]
            if product > max_product:
                max_product = product
            if i != 0:
                # lower anti-diagonals
                product = grid[(rows-1)-j][j+i] * grid[(rows-1)-j-1][j+i+1] * grid[(rows-1)-j-2][j+i+2] * grid[(rows-1)-j-3][j+i+3]
                if product > max_product:
                    max_product = product
    print max_product
    # 70600674