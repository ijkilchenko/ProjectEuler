import math

def GenPrimes(n): #Prints/returns primes up to (n-1) hundreds. 
    numbersL= [i for i in range(1, int(1*math.pow(10,n)+1))]
    currentP= numbersL[1]

    #print(numbersL)
    #print(currentP)
    #print(len(numbersL))

    while (currentP <= len(numbersL)):
        i= 2
        while (currentP*i <= len(numbersL)):
            numbersL[currentP*i-1]= 0
            i= i+1
        j= 1
        if (currentP + j >= len(numbersL)):
            break
        while (numbersL[currentP + j -1] == 0):
            j= j+1
            if (currentP + j >= len(numbersL)):
                break
        currentP= currentP + j
        #print(currentP)

        
        
    #print(numbersL)
    #print(currentP)
    #print(numbersL)
    #print(sum(numbersL)-1)

    numbersC= []
    for i in range (1, len(numbersL)):
        if (numbersL[i] != 0):
            numbersC.append(numbersL[i])
    
    #print(numbersC)
    return numbersC

def CountDivisors(n, Primes):
    i= 0
    number= n
    totald= 1
    total= 0

    while (number >= 2):
        total= 1
        #print(Primes[i])
        while (number%Primes[i]==0):
            number= number/Primes[i]
            total= total + 1
        #print(total)
        if (total > 0):
            totald= totald*total
        i= i+1
    #print(totald)
    if (totald >= 500):
        return 1
    return 0
    #print(totald)

def run():
    Primes= GenPrimes(5)

    i= 1
    n= 1
    while (CountDivisors(n, Primes) != 1):
        #print(n)
        i= i + 1
        n= i*(i+1)/2

    print(i)
    print(n)
    #CountDivisors(95600, Primes)

run()
print("Done!")
#GenPrimes(2)
