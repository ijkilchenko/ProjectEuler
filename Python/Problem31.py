d = {}

def getNum(n):
    try :
        return d[n]
    except KeyError :        
        num = 1
        if (n == 0):
            num = 1
        if (n > 0 and n < 2):
            num = getNum(n - 1)
        if (n >= 2 and n < 5):
            num = getNum(n - 2) + getNum(n - 1)
        if (n >= 5 and n < 10):
            num = getNum(n - 5) + getNum(n - 2) + getNum(n - 1)
        if (n >= 10 and n < 20):
            num = getNum(n - 10) + getNum(n - 5) + getNum(n - 2) + getNum(n - 1)
        if (n >= 20 and n < 50):
            num = getNum(n - 20) + getNum(n - 10) + getNum(n - 5) + getNum(n - 2) + getNum(n - 1)
        if (n >= 50 and n < 100):
            num = getNum(n - 50) + getNum(n - 20) + getNum(n - 10) + getNum(n - 5) + getNum(n - 2) + getNum(n - 1)
        if (n >= 100 and n < 200):
            num = getNum(n - 100) + getNum(n - 50) + getNum(n - 20) + getNum(n - 10) + getNum(n - 5) + getNum(n - 2) + getNum(n - 1)
        if (n == 200):
            num = getNum(n - 200) + getNum(n - 100) + getNum(n - 50) + getNum(n - 20) + getNum(n - 10) + getNum(n - 5) + getNum(n - 2) + getNum(n - 1)
        d[n] = num
        return num

print(getNum(5))
