base = [
"",
"one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine",
"ten",
"eleven",
"twelve",
"thirteen",
"fourteen",
"fifteen",
"sixteen",
"seventeen",
"eighteen",
"nineteen",
"twenty",
"thirty",
"forty",
"fifty",
"sixty",
"seventy",
"eighty",
"ninety"
]

msum = 0

for number in range(1,1001):
    final = ""
    if (number == 1000):
        final = "onethousand"
    number %= 1000
    if (number/100 != 0):
        final += str(base[number/100]) + "hundred"
        number %= 100
        if (number <= 20 and number > 0):
            final += "and" + str(base[number])
        elif (number != 0):
            final += "and" + str(base[number/10 + 18]) + str(base[number%10])
    else:
        number %= 100
        if (number <= 20 and number > 0):
            final += str(base[number])
        elif (number != 0):
            final += str(base[number/10 + 18]) + str(base[number%10])
    msum += len(final)
print msum
# 21124