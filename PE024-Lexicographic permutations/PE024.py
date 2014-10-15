# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120
# 201   210 What is the millionth lexicographic permutation of the digits 0,
# 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Heap's Algorithm
#https://en.wikipedia.org/wiki/Heap's_algorithm

def create_permutations(flength, flist_of_chars):
        if flength == 1:
            final_list.append("".join(str(x) for x in flist_of_chars))
        else:
            for i in xrange(flength):
                create_permutations(flength-1, flist_of_chars)
                if flength % 2 == 1:
                    c = 0
                else:
                    c = i
                temp = flist_of_chars[c]
                flist_of_chars[c] = flist_of_chars[flength-1]
                flist_of_chars[flength-1] = temp

list_of_chars = range(10)
length = len(list_of_chars)
final_list = []
create_permutations(length, list_of_chars)
final_list.sort()
print final_list[1000000 - 1]
# 2783915460