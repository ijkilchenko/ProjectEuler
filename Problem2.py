"""
Author: Alexey Ilchenko
Problem 2 of Project Euler
"""

import math

def nextfib(f1, f2):
    return f1 + f2
    
def run():
    #We define the first two Fibonacci numbers.
    f_1= 1
    f_2= 1
    summa= 0#The sum of even Fibonacci numbers given the first two numbers.
    f_1= nextfib(f_1, f_2)
    while (f_1 < 4*math.pow(10,6)):
        if (f_1%2 == 0):
            summa= summa + f_1
        temp= f_1
        f_1= nextfib(f_1, f_2)
        f_2= temp
    print(summa)

run()
