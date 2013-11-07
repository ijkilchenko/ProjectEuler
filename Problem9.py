import math

def checktriple(a,b,c):
    #print(c)
    #print(math.pow(a,2)+math.pow(b,2)-math.pow(c,2))
    return not(math.pow(a,2)+math.pow(b,2)-math.pow(c,2))    

def checksum(a,b,c):
    return not(a+b+c-1000)

def run():
    i= 1
    #j= 2
    #k= 3

    while (i < 1000):
        j= i+1
        while (j < 1000):
            k= 1000-i-j
            #print(k)
            if (checktriple(i,j,k) == True):
                print("Success")
                print(i)
                print(j)
                print(k)
                print(i*j*k)
            j=j+1
        i=i+1

    #print(i)
    #print(j)
    #print(k)

    #print(checktriple(3,4,5))
    
run()
