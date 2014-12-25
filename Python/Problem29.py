import math

def getDistinctPowers():
    l =[]

    for i in range(2, 101):
        for j in range(2, 101):
            num = math.pow(i,j)
            try:
                l.index(num)
            except ValueError:
                l.append(num)

    return len(l)

print(getDistinctPowers())
