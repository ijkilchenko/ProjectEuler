import math

def isPalindromic(n):
    n = str(n)
    for i in range(0, math.floor(len(n)/2)):
        if (n[i] != n[-(i+1)]):
            return False
    return True

def isBinPalindromic(n):
    binaryLength = math.floor(math.log(n, 2)) + 1
    binary = ''
    for i in range(1, binaryLength + 1):
        if (math.floor(n/math.pow(2, binaryLength-i)) > 0):
            binary = binary + '1'
        else:
            binary = binary + '0'
        n = n - math.floor(n/math.pow(2, binaryLength-i))*math.pow(2, binaryLength-i)
    for i in range(0, math.floor(binaryLength/2)):
        if (binary[i] != binary[-(i+1)]):
            return False
    
    return True

def solve():
    sum = 0
    for i in range (1, 1000000):
        if (isPalindromic(i) and isBinPalindromic(i)):
            sum = sum + i
    return sum

print(solve())
