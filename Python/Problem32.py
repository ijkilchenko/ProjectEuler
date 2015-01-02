def findIdentities(n):
    st= ''.join(n)
    i = 1
    l = []
    while (i < 9 - 2):
        j = i + 1
        while (j < 9 - 1):
            left = int(st[:i])
            middle = int(st[i:j])
            right = int(st[j:])
            if (left * middle == right):
                l.append(right)
            j = j + 1
        i = i + 1
    return l

def findPandigitalProducts():
    l = []
    count = 0
    z = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    r = permuteList(z)
    for i in r:
        count = count + 1
            
        m = findIdentities(i)
        for j in m:
            try:
                l.index(j)
            except ValueError:
                l.append(j)
            
    total = 0
    for i in l:
        total = total + i
    
    print(l)
    print(count)
    print(total)

def permuteList(l):
    if not l:
            return [[]]
    res = []
    for e in l:
            temp = l[:]
            temp.remove(e)
            res.extend([[e] + r for r in permuteList(temp)])

    return res

findPandigitalProducts()
