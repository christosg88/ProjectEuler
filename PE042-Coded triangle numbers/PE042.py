# The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2;
# so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value. For
# example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
# value is a triangle number then we shall call the word a triangle word.
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
# containing nearly two-thousand common English words, how many are triangle
# words?

with open("words.txt", "r") as words:
    triangle_words = 0
    triangle_numbers = [1]
    max_triangle_number = 1
    n = 1
    line = words.readline()
    list_of_words = line.split(",")
    number_of_words = len(list_of_words)
    value_of_words = [0 for x in xrange(number_of_words)]
    for i in xrange(number_of_words):
        for j in xrange(len(list_of_words[i])):
            value_of_words[i] += ord(list_of_words[i][j]) - ord('A') + 1
        while value_of_words[i] > max_triangle_number:
            n += 1
            max_triangle_number = (n*(n+1))/2
            triangle_numbers.append(max_triangle_number)
        for triangle_number in triangle_numbers:
            if value_of_words[i] == triangle_number:
                triangle_words += 1
    print triangle_words
# 162