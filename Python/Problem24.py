"""
Author: Alexey Ilchenko
Problem 24 of Project Euler
"""
import math
import itertools

def run():
    l='0123456789'
    k= len(l)
    m= 0
    i= 1
    for p in itertools.permutations(l,k):
        if (i == 1000000):
            m= "".join(p)
        #print "".join(p)
        i= i + 1
    print(m)
        

run()
