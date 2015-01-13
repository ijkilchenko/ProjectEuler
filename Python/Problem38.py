import math

def isConcatenation(pan):
    st = str(pan)
    for l in range(1, len(st)):
        num = int(st[0:l])
        j = 2
        result = num * j
        length = len(str(result))
        i = len(str(num))
        while (i < len(st) and result == int(st[i: i + length])):
            i = i + length
            j = j + 1
            result = num * j
            length = len(str(result))
        if (i == len(st)):
            return True
    return False

def permuteList(l):
    if (len(l) == 0):
            return ['']
    res = []
    for e in l:
            temp = l
            temp = temp.replace(e, '')
            r = permuteList(temp)
            for i in r:
                res.append(e + i)
    return res

def solve():
    z = '987654321'
    r = permuteList(z)
    for n in r:
        if (isConcatenation(n)):
            print(n)

solve()
    
#print(isConcatenation(918273645)) # True
