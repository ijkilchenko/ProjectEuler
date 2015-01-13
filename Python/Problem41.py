import utilsPrimes as utils

def getPandigitalList(n):
    l = '987654321'
    l = l[9-n:9]

    l = permuteList(l)
    return l

def permuteList(l):
    if (l == ''):
        return []
    else :
        r = []
        for s in l:
            temp = l
            temp = temp.replace(s, '')
            k = permuteList(temp)
            if (k == []):
                r.append(s)
            for i in k:
                r.append(s + i)
        return r

def solve():
    for i in range(0, 9):
        l = getPandigitalList(i+1)
        for j in l:
            if (utils.isPrime(int(j))):
                print(j)
                break
        print(i)

solve()
