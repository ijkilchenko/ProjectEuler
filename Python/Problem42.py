import math

def getWords():
    f= open ("./p042_words.txt","r")
    s= []
    cString= f.readline()
    while (cString != ""):
        s.append(cString)
        cString= f.readline()
    s = s[0]
    s = s.replace('"', '')
    s = s.lower()
    s = s.split(',')
    return s

def getWordValue(w):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    sum = 0
    for i in w:
        sum = sum + alpha.index(str(i)) + 1
    return sum

def isTriangleNum(t):
    n1 = (-1 + math.sqrt(1 + 8*t))/2
    n2 = (-1 - math.sqrt(1 + 8*t))/2
    if (n1 == math.floor(n1) or n2 == math.floor(n2)):
        return True
    else:
        return False

def solve():
    l = getWords()
    count = 0
    for w in l:
        v = getWordValue(w)
        if (isTriangleNum(v)):
            count = count + 1
    return count

#print(getWordValue('sky'))
#print(isTriangleNum(6))
print(solve())
