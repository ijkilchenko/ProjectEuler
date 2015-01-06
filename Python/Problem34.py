import functools
import math

fac = {}
fac[0] = 1
fac[1] = 1
fac[2] = 2

def fact(n):
    try:
        return fac[n]
    except KeyError:
        fac[n] = functools.reduce(lambda x,y: x*y, range(1, n+1))
        return fac[n]

def checkNum(n):
    digits = str(n)
    for d in digits:
        if (n < 0):
            return False
        else:
            n = n - fact(int(d))
    if (n == 0):
        return True
    else:
        return False
    
def sumSpecials():
    total = 0
    for i in range(3, int(math.pow(10,7) - 1)):
        if (checkNum(i)):
            total = total + i
    print(total)

sumSpecials()
