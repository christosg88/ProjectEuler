# A unit fraction contains 1 in the numerator. The decimal representation of
# the unit fractions with denominators 2 to 10 are given:
# 1/2 =   0.5
# 1/3 =   0.(3)
# 1/4 =   0.25
# 1/5 =   0.2
# 1/6 =   0.1(6)
# 1/7 =   0.(142857)
# 1/8 =   0.125
# 1/9 =   0.(1)
# 1/10    =   0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
# seen that 1/7 has a 6-digit recurring cycle. Find the value of d < 1000 for
# which 1/d contains the longest recurring cycle in its decimal fraction part.

def next_decimal(over, under):
    return int((10*over) / under)

max_length = 0
num_with_max_length = 0
# goes through 2 to 999
for i in xrange(2,1000):
    num = 1.0
    cyclic = True
    decimals = []
    count_decimals = 0
    cycled = False
    while num != 0 and cyclic:
        if num % i != 0:
            current_decimal = next_decimal(num, i)
            decimals.append(current_decimal)
            count_decimals += 1
            num = (10*num) % i
            if count_decimals > 1:
                for x in xrange(0,count_decimals-1):
                    if decimals[x] == current_decimal:
                        start = x
                        end = count_decimals-1
                        if end - start > 1:
                            cycled = True
                            for y in xrange(end-start):
                                if decimals[start+y] != decimals[end+y]:
                                    cycled = False
                                    break
                                current_decimal = next_decimal(num, i)
                                decimals.append(current_decimal)
                                count_decimals += 1
                                num = (10*num) % i
                            if cycled:
                                if end-start == 2 and decimals[start] == decimals[start+1]:
                                    length = end-start-1
                                else:
                                    length = end-start
                                if length > max_length:
                                    max_length = length
                                    num_with_max_length = i
                                break
            if cycled:
                break                    
        else:
            cyclic = False
print num_with_max_length, max_length
# 983 982