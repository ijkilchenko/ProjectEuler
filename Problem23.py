"""
Author: Alexey Ilchenko
Problem 23 of Project Euler
"""

import math

def run():
    n= 28123+1
    #n= 12+1

    abundants= set()
    for i in range(12, n):
        sum= 0
        for j in range(1, int(math.floor((i+1)/2)) + 1):
            if (i%j == 0):
                sum += j
        if (sum > i):
            abundants.add(i)

    sum_of_abundants= set()
    for i in abundants:
        for j in abundants:
            sum_of_abundants.add(i+j)

    none_sum= set(range(1, n)).difference(sum_of_abundants)
    #print(sum_of_abundants)
    #print(none_sum)
    sum= 0
    for i in none_sum:
        sum += i
    print(sum)
            
run()
