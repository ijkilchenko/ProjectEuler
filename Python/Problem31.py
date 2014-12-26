d = {}

def getNums(n):
    return getNum(n, 0, 0, 0, 0, 0, 0, 0, 0)

def getNum(n, i, j, k, l, m, o, p, q):
    total = i + 2*j + 5*k + 10*l + 20*m + 50*o + 100*p + 200*q
    try:
        if (d[n] > 0):
            return d[n]
    except KeyError :
        num = 1
        if (n == 0):
            num = 1
        if (n > 0 and n < 2):
            num = getNum(n - 1, i + 1, j, k, l, m, o, p, q)
        if (n >= 2 and n < 5):
            num = getNum(n - 2, i, j + 1, k, l, m, o, p, q) + getNum(n - 1, i + 1, j, k, l, m, o, p, q)
        if (n >= 5 and n < 10):
            num = getNum(n - 5, i, j, k + 1, l, m, o, p, q) + getNum(n - 2, i, j + 1, k, l, m, o, p, q) + getNum(n - 1, i + 1, j, k, l, m, o, p, q)
        if (n >= 10 and n < 20):
            num = getNum(n - 10, i, j, k, l + 1, m, o, p, q) + getNum(n - 5, i, j, k + 1, l, m, o, p, q) + getNum(n - 2, i, j + 1, k, l, m, o, p, q) + getNum(n - 1, i + 1, j, k, l, m, o, p, q)
        if (n >= 20 and n < 50):
            num = getNum(n - 20, i, j, k, l, m + 1, o, p, q) + getNum(n - 10, i, j, k, l + 1, m, o, p, q) + getNum(n - 5, i, j, k + 1, l, m, o, p, q) + getNum(n - 2, i, j + 1, k, l, m, o, p, q) + getNum(n - 1, i + 1, j, k, l, m, o, p, q)
        if (n >= 50 and n < 100):
            num = getNum(n - 50, i, j, k, l, m, o + 1, p, q) + getNum(n - 20, i, j, k, l, m + 1, o, p, q) + getNum(n - 10, i, j, k, l + 1, m, o, p, q) + getNum(n - 5, i, j, k + 1, l, m, o, p, q) + getNum(n - 2, i, j + 1, k, l, m, o, p, q) + getNum(n - 1, i + 1, j, k, l, m, o, p, q)
        if (n >= 100 and n < 200):
            num = getNum(n - 100, i, j, k, l, m, o, p + 1, q) + getNum(n - 50, i, j, k, l, m, o + 1, p, q) + getNum(n - 20, i, j, k, l, m + 1, o, p, q) + getNum(n - 10, i, j, k, l + 1, m, o, p, q) + getNum(n - 5, i, j, k + 1, l, m, o, p, q) + getNum(n - 2, i, j + 1, k, l, m, o, p, q) + getNum(n - 1, i + 1, j, k, l, m, o, p, q)
        if (n == 200):
            num = getNum(n - 200, i, j, k, l, m, o, p, q + 1) + getNum(n - 100, i, j, k, l, m, o, p + 1, q) + getNum(n - 50, i, j, k, l, m, o + 1, p, q) + getNum(n - 20, i, j, k, l, m + 1, o, p, q) + getNum(n - 10, i, j, k, l + 1, m, o, p, q) + getNum(n - 5, i, j, k + 1, l, m, o, p, q) + getNum(n - 2, i, j + 1, k, l, m, o, p, q) + getNum(n - 1, i + 1, j, k, l, m, o, p, q)
        d[total] = num
        return num

print(getNums(5))
