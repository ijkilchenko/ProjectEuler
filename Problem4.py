"""
Author: Alexey Ilchenko
Problem 4 of Project Euler
"""

import math

#Find the largest palindrome made from the product of two 3-digit numbers. 
#Upper limit is 999*999.

def palindromeness(n):
    mystring= str(n)
    mylength= len(mystring)
    for i in range(1,mylength):
        if (mystring[i] != mystring[mylength-1-i]):
            return 0
    return 1

def run():
    largest= 0
    current= 0
    upperlimit= 999*999
    left= 0
    right= 0
    for i in range(1, 1000):
        for j in range(1, 1000):
            if (palindromeness(current) == 1 and current > largest):
                largest= current
            current= i *j

    print(largest)

run()
