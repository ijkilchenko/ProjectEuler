"""
Author: Alexey Ilchenko
Problem 454 of Project Euler INCOMPLETE
"""
import math

def run():
    power= 4
    L= int(math.pow(10,power))
    #l= [0 for i in range(0,L)]
    c= 0
    for j in range(2,L+1):
        for i in range(1,j):
            if ((i*j)%(i+j) == 0):
                #print(str(i)+ " " +str(j))
                #print(float(j)/i)
                #l[int(float(j)/i)]= 1
                c= c + 1
    #print(l)
    print(c)

"""
    c= 0
    for j in range(2,L+1):
        for i in range(1,j):
            k= math.log(float(i*j)/(i+j))
            k= math.pow(math.e, k)
            tol= 0.001
            if (k-math.floor(k) < tol or k-math.floor(k) > 1-tol):
                #print(str(i)+ " " +str(j))
                c= c + 1

    print(c)
"""

run()
