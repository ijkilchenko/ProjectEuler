"""
Author: Alexey Ilchenko
Problem 3 of Project Euler
"""

import math

def primeness(newterm, P):
    for k in range(1, len(P)):
        if (newterm%P[k] == 0):
            return 0
    return newterm

def nextprime(P):
    last= P[len(P)-1]
    newterm= last+2
    while (primeness(newterm, P) == 0):
        newterm= newterm + 2
        #print(newterm)
    return newterm

def run():
    P= [2, 3]
    i= 1
    number= 600851475143

    while (number/P[i] >= 2):
        while (number%P[i]==0):#Divide by a single prime as many times we can.
            #Left with a product of less number of smaller factors.
            number= number/P[i]            
        P.append(nextprime(P))#Calculate next prime given previous primes. 
        i= i+1
        
    print(number)
    #print(P[len(P)-1])

run()

"""
Notable alternatives

(I.)

roots = []; product = 1; x = 2; number = input("number?: "); y = number
while product != number:
   while (y % x == 0):
      roots.append(x)
      y /= x
      product *= roots[-1]
   x += 1
print roots


(II.)
primes = set([2])
value = 3
number = 317584931803
while value < sqrt(number):
    isPrime = True
    for k in primes:
        if value % k == 0:
            isPrime = False
            value += 2
    if isPrime:
        primes.add(value)
        if number % value == 0:
            print value
            number /= value
print number
"""
