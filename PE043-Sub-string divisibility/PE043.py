# The number, 1406357289, is a 0 to 9 pandigital number because it is made up
# of each of the digits 0 to 9 in some order, but it also has a rather
# interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we
# note the following:
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.


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

final_list = []
list_of_chars = range(10)
length = len(list_of_chars)
create_permutations(length, list_of_chars)
sum = 0
primes = [2, 3, 5, 7, 11, 13, 17]
for i in xrange(len(final_list)):
    is_divisible = True
    for k in xrange(1,8):
        if int(final_list[i][k:k+3]) % primes[k-1] != 0:
            is_divisible = False
    if is_divisible:
        sum += int(final_list[i])
print sum
# 16695334890