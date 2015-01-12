import utilsPrimes as utils
import math

def getListOfTruncations(n):
    l = []
    n = str(n)
    l.append(n)
    length = len(n)
    for i in range(1, length):
        l.append(n[:i])
        l.append(n[i:])
    
    return l

def solve():
    count = 1
    summ = 0
    i = 11
    while (count <= 11):
        l = getListOfTruncations(i)
        flag = True
        for n in l:
            if (not utils.isPrime(int(n))):
                flag = False
                break
        if (flag == True):
            summ = summ + i
            count = count + 1
        i = i + 1
    return summ

print(solve())
