"""https://www.codewars.com/kata/52f3149496de55aded000410/train/python"""

# Summing a number's digits

def sum_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum

# 1 mistake 