import math

def getDigit(d):
    d = d - 1
    ran = 1
    while (d > 0):
        d = d - 9*math.pow(10, ran-1)*ran
        ran = ran + 1
    ran = ran - 1
    d = d + 9*math.pow(10, ran-1)*ran
    num = math.floor((d+1)/ran)
    for i in range(1, ran):
        num = num + 9*math.pow(10, i-1)
    digit = math.floor(d%ran)
    num = math.floor(num)
    num = str(num)[int(digit)]
    return num

def solve():
    product = 1
    for i in range(1, 6):
        product = product * int(getDigit(math.pow(10, i)))
    return product

print(solve())
