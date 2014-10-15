# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
# 71, 73, 79, and 97.
# How many circular primes are there below one million?

def is_prime(num):
    if num <= 1 or (num % 2 == 0 and num != 2):
        return False
    else:
        for i in xrange(2,int(num**0.5)+1):
            if num % i == 0:
                return False
    return True

def create_rotations(flength, flist_of_chars):
        for i in xrange(1,flength):
            ftemp = flist_of_chars[0]
            for j in xrange(0, flength-1):
                flist_of_chars[j] = flist_of_chars[j+1]
            flist_of_chars[flength-1] = ftemp
            final_list.append("".join(str(x) for x in flist_of_chars))

counter = 0
for number in xrange(2,1000000):
    if is_prime(number):
        flag = True
        final_list = []
        list_of_chars = []
        temp = number
        while temp != 0:
            list_of_chars.insert(0, temp % 10)
            temp = temp / 10
        length = len(list_of_chars)
        create_rotations(length, list_of_chars)
        for n in final_list:
            if not is_prime(int(n)):
                flag = False
                break
        if flag:
            counter += 1
            # print "%2d. %d" %(counter, number)

print counter
# 55