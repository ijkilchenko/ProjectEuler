import math

def isPentagonal(p):
    n1 = (1 + math.sqrt(1 + 4*3*2*p))/6
    n2 = (1 - math.sqrt(1 + 4*3*2*p))/6
    if (n1 == math.floor(n1) and n1 > 0 or n2 == math.floor(n2) and n2 > 0):
        return True
    else:
        return False

def isTriangular(t):
    n1 = (-1 + math.sqrt(1 + 8*t))/2
    n2 = (-1 - math.sqrt(1 + 8*t))/2
    if (n1 == math.floor(n1) and n1 > 0 or n2 == math.floor(n2) and n2 > 0):
        return True
    else:
        return False

def isHexagonal(h):
    n1 = (1 + math.sqrt(1 + 8*h))/4
    n2 = (1 - math.sqrt(1 + 8*h))/4
    if (n1 == math.floor(n1) and n1 > 0 or n2 == math.floor(n2) and n2 > 0):
        return True
    else:
        return False

def isSpecial(n):
    if (isPentagonal(n) and isHexagonal(n)):
        return True
    else:
        return False

def solve():
    i = 286
    n = (i*(i + 1))/2
    while (not isSpecial(n)):
        i = i + 1
        n = (i*(i + 1))/2
    return n

print(solve())
