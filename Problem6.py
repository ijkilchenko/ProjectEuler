import math

def sumsquare(n):
    sum= 0
    for i in range(1,n+1):
        sum= sum + math.pow(i,2)
    return sum

def squaresum(n):
    return math.pow(n*(n+1)/2,2)

def run():
    #print(squaresum(3))
    print(squaresum(100)-sumsquare(100))

run()
