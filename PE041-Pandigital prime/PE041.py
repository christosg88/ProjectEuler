# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime.
# What is the largest n-digit pandigital prime that exists?

def isPrime(number):
    if number <= 3:
        if number <= 1:
            return False
        return True
    if not number % 2 or not number % 3:
        return False
    for i in range(5, int(number ** 0.5) + 1, 6):   
        if not number % i or not number % (i + 2):
            return False
    return True

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

max_number = 0
for x in xrange(2,10):
    list_of_chars = range(1,x)
    length = len(list_of_chars)
    final_list = []
    create_permutations(length, list_of_chars)
    for number in final_list:
        if isPrime(int(number)):
            if number > max_number:
                max_number = number
print max_number
# 7652413