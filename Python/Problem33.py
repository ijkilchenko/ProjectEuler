import math

def solve():
    i = 11
    numT = 1
    denT = 1
    while (i < 100):
        j = i * 2
        while (j < 100):
            num = str(i)
            den = str(j)
            one = num[0]
            two = num[1]
            if (int(num) % 10 != 0 and int(den) % 10 != 0):
                try:
                    if (den.index(one) >= 0):
                        oneI = den.index(one)
                        numP = i%10
                        denP = int(den[1-oneI])
                        if (int(den) != 0 and int(denP) != 0):
                            if (int(num)/int(den) == int(numP)/int(denP)):
                                numT = numT * numP
                                denT = denT * denP
                except ValueError:
                    print()
                try:
                    if (den.index(two) >= 0):
                        oneI = den.index(two)
                        numP = math.floor(i/10)
                        denP = int(den[1-oneI])
                        if (int(den) != 0 and int(denP) != 0):
                            if (int(num)/int(den) == int(numP)/int(denP)):
                                numT = numT * numP
                                denT = denT * denP
                except ValueError:
                    print()
            j = j + 1
        i = i + 1
    print(numT)
    print(denT)

solve()
                
                    
