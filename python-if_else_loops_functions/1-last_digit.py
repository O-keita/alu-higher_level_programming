#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
str_number = num[-1]
last_number = int(str_number)
if number > 5 < last_number:
    print(f"Last digit of {number} is {last_number}\
 and is greater than 5")
elif 0 < number < 5 < last_number:
    print(f"Last digit of {number} is -{last_number}\
 and is greater than 5")

elif number == 0:
    print(f"Last digit of {number} is\
 {last_number} and is 0")
elif number > 0 < last_number < 6:
    print(f"Last digit of {number} is {last_number}\
 and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is -{last_number}\
 and is less than 6 and not 0")
