# An irrational decimal fraction is created by concatenating the positive
# integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the
# following expression.
# d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

number = 1
str_num = ""
while len(str_num) < 1000000:
    str_num = str_num + str(number)
    number += 1

mul = int(str_num[1-1]) * int(str_num[10-1]) * int(str_num[100-1]) * \
int(str_num[1000-1]) * int(str_num[10000-1]) * int(str_num[100000-1]) * int(str_num[1000000-1])

print mul
# 210