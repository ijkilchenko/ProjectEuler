def NextNum(n):
    if (n%2 == 0):
        return n/2
    return 3*n+1

def run():

    Tchain= 0
    Cchain= 0
    startnum= 0

    for i in range (1, 1000000):
        n= i
        Cchain= 0
        while (NextNum(n) != 1):
            n= NextNum(n)
            Cchain= Cchain+1
        if (Cchain >= Tchain):
            startnum= i
            Tchain= Cchain

    print(startnum)
    print(Tchain)

run()
