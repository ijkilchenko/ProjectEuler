global primes
primes = [2, 3, 5, 7, 11, 13, 17]

def getListOfPermutations(string):
    if (len(string) == 0):
        return ['']
    else:
        l = []
        for e in string:
            temp = string
            temp = temp.replace(e, '')
            ll = getListOfPermutations(temp)
            if (ll == ['']):
                l.append(e)
            else:
                for i in ll:
                    s = e + i
                    if (len(s) >= 3 and len(s) != 10):
                        j = len(s)-3
                        num = int(s[0:3])
                        if (num % primes[len(primes)-1-j] == 0):
                            l.append(s)
                    else:
                        l.append(s)
        return l

def getNPandigitals(n):
    l = '0987654321'
    l = l[10-n:10]
    return getListOfPermutations(l)

def solve():
    l = getNPandigitals(10)
    print(l)
    print(len(l))
    s = 0
    
    for n in l:
        s = s + int(n)
    return s

print(solve())
