import math

def isNumSumOfDigits(n):
    sum = 0
    l = len(str(n))
    for i in range(0, l):
        sum = sum + math.pow(int(str(n)[i]), 5)
    if (sum == n):
        return True
    else :
        return False

def getAllNums(l):
    sum = 0
    start = 11
    finish = math.pow(10,7)
    for i in range(int(start), int(finish)):
        if (isNumSumOfDigits(i)):
            sum = sum + i

    return sum

#print(isNumSumOfDigits(9474))
#print(isNumSumOfDigits(9999))
print(getAllNums(5))


