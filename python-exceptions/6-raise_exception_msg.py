#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
         raise TypeError("C is fun")
     except TypeError:
         print("C is fun")
