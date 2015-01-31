def getListOfPermutations(string):
    if (len(string) == 0):
        return ['']
    else:
        l = []
        for j in range(0, len(string)):
            temp = string[:j] + string[j+1:]
            ll = getListOfPermutations(temp)
            if (ll == ['']):
                l.append(string[j])
            else:
                for i in ll:
                    s = string[j] + i
                    l.append(s)
        return l

def getNPandigitals(n):
    l = '0987654321'
    l = l[10-n:10]
    return getListOfPermutations(l)

def isPermutation(a, b):
    if (len(a) != len(b)):
        return False
    for i in a:
        if (not(i in b)):
            return False
        else:
            j = b.index(i)
            b = b[0:j] + b[j+1:]
    return True

#print(getNPandigitals(4))

print(isPermutation("1231", "3211"))


