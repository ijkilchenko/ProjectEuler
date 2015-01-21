import utilsPrimes as u
import math

def getSubsets(length):
    l = []
    for i in range(1, math.floor(math.pow(2, length))):
        l.append(toBinary(i))
    return l

def toBinary(n):
    b = []
    while (n > 0):
        i = 0
        while (math.pow(2, i + 1) <= n):
            i = i + 1
        n = n - math.pow(2, i)
        b.append(i)
    return b

def solve():
    p = 223
    condition = True
    l = getSubsets(len(str(p)))
    lastLength = len(str(p))
    while (condition):
        print(p)
        st = str(p)
        if (lastLength != len(str(p))):
            l = getSubsets(len(str(p)))
            lastLength = len(str(p))
        for i in l:
            count = 0
            z = []
            for j in range(0, 10):
                newSt = st
                for k in i:
                    newSt = newSt[:k] + str(j) + newSt[k+1:]
                num = int(newSt)
                if (num != 0 and math.floor(math.log(num, 10)) + 1 != len(newSt)):
                    continue
                if (u.isPrime(int(newSt))):
                    count = count + 1
                    z.append(newSt)
                if (j > 2 and count < j - 2):
                    break
                if (count == 8):
                    condition = False
                    print(p, z)
        p = u.nextPrime(p)

solve()

                    
