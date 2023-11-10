#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    try:
      for i in range(1, 3):
        if i > a:
          raise Exception('Too far')
        result += (a ** b) / i
    except Exception: 
      # If an exception is raised, simply add a and b.
      result = a + b

    return result
