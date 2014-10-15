# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.

columns = 50
rows = 100
number = [[0 for i in xrange(columns)] for i in xrange(rows+1)]

with open("number.txt") as number_file:
    for i in xrange(rows):
        line = (number_file.readline()).strip("\n")
        for j in xrange(columns):
            number[i][j] = int(line[j])
            number[rows][j] += int(line[j])

    for i in xrange(columns-1):
        number[rows][columns-2-i] += number[rows][columns-1-i] / 10
        number[rows][columns-1-i] %= 10


    final = ""
    for i in xrange(columns):
        final += str(number[rows][i])

    print final[:10]
    # 5537376230