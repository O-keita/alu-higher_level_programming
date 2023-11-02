#!/usr/bin/python3
def fizzbuzz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 ==0:
            print ("FizzBuzz", end = " ")
        elif num % 3 == 0:
            num = "Fizz"
            print("{}".format(num), end = " ")
        elif num % 5 == 0:
            print("Buzz", end = " ")
        else:
            print(num, end = " ")

fizzbuzz()
