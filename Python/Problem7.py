import math

def primeness(newterm, P):
    for k in range(1, len(P)):
        if (newterm%P[k] == 0):
            return 0
    return newterm

def nextprime(P):
    last= P[len(P)-1]
    newterm= last+2
    while (primeness(newterm, P) == 0):
        newterm= newterm + 2
        #print(newterm)
    return newterm

def run():
    P= [2, 3]
    i= 1
    
    while (len(P) <= 10000):
        P.append(nextprime(P))
        i= i+1
        
    print(P[len(P)-1])

run()
