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
                    l.append(s)
        return l

def getNPandigitals(n):
    l = '0987654321'
    l = l[10-n:10]
    return getListOfPermutations(l)

#print(len(getNPandigitals(10)))


