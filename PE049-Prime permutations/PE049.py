# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms are
# prime, and, (ii) each of the 4-digit numbers are permutations of one
# another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
# primes, exhibiting this property, but there is one other 4-digit increasing
# sequence.
# What 12-digit number do you form by concatenating the three terms in this
# sequence?

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

def isPermutation(number1, number2):
    list_of_ints = map(int,final_list)
    if (number1 in list_of_ints):
        if (number2 in list_of_ints):
            return True
    return False

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

number = 1001
while number < 10000:
    if isPrime(number):
        # print ("~%d" %number)
        i = 1000
        final_list = []
        create_permutations(4, list(str(number)))
        while number+(2*i) < 10000:
            if isPrime(number+i):
                if isPrime(number+(2*i)):
                    if isPermutation(number+i,number+2*i):
                        print ("n = %d" %number)
                        print ("i = %d" %i)
                        print str(number)+str(number+i)+str(number+2*i)+"\n"
            i += 2
    number += 2
# 296962999629