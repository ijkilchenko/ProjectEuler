import math

def run(n):
    sum = 1
    corner = 1
    i = 2
    while (corner <= n**2):
        corner = getTopRightCorner(i)
        sum = sum + corner
        sum = sum + corner  - 2*(i-1)
        sum = sum + corner  - 2*2*(i-1)
        sum = sum + corner  - 2*3*(i-1)
        i = i + 1
        
    print(corner)
    print(sum)

def getTopRightCorner(i):
    return (2*(i-1)+1)**2

run(1000)


