"""
Author: Alexey Ilchenko
Problem 26 of Project Euler
"""
import math

def run():
    longest = getDecimalFraction(2)
    d = 3
    while (d < 1000):
        current = getDecimalFraction(d)
        if (current >= longest) :
            longest = current
            print(d)
        d = d + 1
    
    
    return
    
def getDecimalFraction(d):
    p = 10
    lastR = p % d
    l =[]
    newElem = math.floor(p/d)
    l.append(lastR)
    #print(l[-1])
    p = lastR * 10
    
    while (lastR != 0):
        lastR = p % d
        newElem = math.floor(p/d)
        try:
            index = l.index(lastR)
            return (len(l) - index)
        except ValueError:
            l.append(lastR)
            #print(l[-1])
            p = lastR * 10

    try:
        newElem = math.floor(p/d)
        index = l.index(lastR)
        return (len(l) - index)
    except ValueError:
        return 0
    
#run()
print(getDecimalFraction(41))

