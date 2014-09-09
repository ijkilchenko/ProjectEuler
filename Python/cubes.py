import math
def run():
    i= 1
    j= 2
    n= 200000
    A= [0]*n

    while (math.pow(i,3) + math.pow(j,3) < n):
        j= 1;
        while (math.pow(i,3) + math.pow(j,3) < n):
            if (A[int(math.pow(i,3) + math.pow(j,3))] > 2):
                print(math.pow(i,3) + math.pow(j,3))
            A[int(math.pow(i,3) + math.pow(j,3))]= A[int(math.pow(i,3)
                                                + math.pow(j,3))] + 1
            j= j + 1
        j= 1
        i= i + 1
run()

