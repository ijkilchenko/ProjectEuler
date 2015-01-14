import math

def isPentagonal(p):
    if (p > 0):
        n1 = (1 + math.sqrt(1 + 4*3*2*p))/6
        n2 = (1 - math.sqrt(1 + 4*3*2*p))/6
        if (n1 == math.floor(n1) and n1 > 0 or n2 == math.floor(n2) and n2 > 0):
            return True
        else:
            return False
    else:
        return False
    
def p(n):
    return n*(3*n - 1)/2

def solve():
    minD = -1
    #guess on the upper bound
    last = 3000
    for i in range(1, last):
        for j in range(i, last):
            s = p(i) + p(j)
            d = p(j) - p(i)
            if (isPentagonal(s) and isPentagonal(d)):
                print(minD, i, j)
                if (d < minD or minD == -1):
                    minD = d
        print(i)
    return minD

print(solve())
    
