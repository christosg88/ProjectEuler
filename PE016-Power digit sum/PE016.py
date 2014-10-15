# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?

number = 2**1000
digit_sum = 0
while number != 0:
    digit_sum += number % 10
    number /= 10
print digit_sum
# 1366