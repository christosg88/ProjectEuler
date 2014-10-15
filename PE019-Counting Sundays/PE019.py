# You are given the following information, but you may prefer to do some
# research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a
# century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?

year = 1900
month = 1
day = 1
week_index = 0
sum_sundays = 0

# from 1/1/1900 to 31/12/2000
while year <= 2000:
    # checks if year is a leap year
    if year % 4 == 0 and year % 100 != 0:
        leap_year = True
    elif (year % 100 == 0 and year % 400 == 0):
        leap_year = True
    else:
        leap_year = False

    while month <= 12:
        # finds how many days the month has
        if month <= 7:
            if month % 2 == 0:
                max_days = 30
            else:
                max_days = 31
        else:
            if month % 2 == 0:
                max_days = 31
            else:
                max_days = 30
        # checks for February
        if month == 2:
            if leap_year:
                max_days = 29
            else:
                max_days = 28

        while day <= max_days:
            if ((day == 1) and (week_index == 6) and (year >= 1901)):
                sum_sundays += 1
            day += 1
            week_index = (week_index + 1) % 7
        # the beginning of new month
        day = 1
        month += 1
    # the beginning of new year
    month = 1
    year += 1
print sum_sundays
# 171