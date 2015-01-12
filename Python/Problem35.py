import utilsPrimes as utils
import math

def getListOfRotations(n):
    l = []
    length = math.floor(math.log(n, 10)) + 1
    for i in range(0, length):
        rem = math.floor(n % math.pow(10, i))
        whole = math.floor(n / math.pow(10,i))
        N = int(str(rem) + str(whole))
        l.append(N)
    return l

def solve():
    count = 0
    for i in range (2, 1000000) :
        l = getListOfRotations(i)
        flag = True
        for n in l:
            if (not utils.isPrime(n)):
                flag = False
                break
        if (flag == True):
            count = count + 1
    return count

print(solve())
