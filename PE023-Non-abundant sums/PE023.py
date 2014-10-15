# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
# number. A number n is called deficient if the sum of its proper divisors is
# less than n and it is called abundant if this sum exceeds n. As 12 is the
# smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that
# can be written as the sum of two abundant numbers is 24. By mathematical
# analysis, it can be shown that all integers greater than 28123 can be
# written as the sum of two abundant numbers. However, this upper limit cannot
# be reduced any further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers is less
# than this limit. Find the sum of all the positive integers which cannot be
# written as the sum of two abundant numbers.

def is_abundant(num):
    m_sum = 0
    for i in range(1, (num / 2) + 1):
        if (num % i == 0):
            m_sum += i
    if m_sum > num:
        return True

LIMIT = 28123
# finds all abundant numbers
abundant_numbers = []
for i in range(1, LIMIT+1):
    if is_abundant(i):
        abundant_numbers.append(i)
print "Found them all."

# finds all sums of abundant numbers
sum_of_abundant = []
len_of_abundant = len(abundant_numbers)
for i in range(len_of_abundant):
    for j in range(i, len_of_abundant):
        sum_of_abundant.append(abundant_numbers[i] + abundant_numbers[j])
sum_of_abundant.sort()

# deletes all sums of abundant numbers
my_list = range(1, LIMIT+1)
index_sum_of_abundant = 0
index_my_list = 0
my_list_length = len(my_list)
# goes through the whole list
while (index_my_list < my_list_length):
    # keep iterating the list
    if my_list[index_my_list] < sum_of_abundant[index_sum_of_abundant]:
        index_my_list += 1
    # until you find a number in the sum list
    elif my_list[index_my_list] == sum_of_abundant[index_sum_of_abundant]:
        # remove the number from the list
        my_list.pop(index_my_list)
        # go to the next different number in the sum list
        index_sum_of_abundant += 1
        while sum_of_abundant[index_sum_of_abundant] == sum_of_abundant[index_sum_of_abundant+1]:
            index_sum_of_abundant += 1
        # find new length of the list
        my_list_length = len(my_list)

print sum(my_list)
# 4179871