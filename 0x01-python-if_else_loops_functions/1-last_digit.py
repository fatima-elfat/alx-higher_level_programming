#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
   r = -number
r %= 10
strr = "Last digit of {} is {}"
if r > 5:
    strr += " and is greater than 5"
elif r == 0:
    strr += " and is 0"
else:
    strr += " and is less than 6 and not 0"
print(strr.format(number, r)) 
