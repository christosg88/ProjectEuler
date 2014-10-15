# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order.
# Then working out the alphabetical value for each name multiply this value by
# its alphabetical position in the list to obtain aname score.
# For example, when the list is sorted into alphabetical order, COLIN, which
# is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?

with open("names.txt", "r") as f:
    total = 0
    line = f.readline()
    names = line.split(",")
    names.sort()
    for i in range(len(names)):
        sum = 0
        for j in range(len(names[i])):
            sum += ord(names[i][j]) - ord('A') + 1
        total += sum * (i+1)
    print total
# 871198282