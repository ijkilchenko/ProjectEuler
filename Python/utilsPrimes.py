import math

primes = []

def isPrime(n) :
    if (n < 2) :
        return False
    else :
        if (n < len(primes)) :
            if (primes[n] == 0) :
                return False
            else :
                return True
        else :
            global primes
            primes = getPrimes(primes)
            return isPrime(n)

def getPrimes(primes) :
    newPrimes = []
    i = 0
    n = 2*len(primes)
    while (i < len(primes)):
        newPrimes.append(primes[i])
        i = i + 1

    while (i < n):
        if (i % 2 == 0):
            newPrimes.append(0)
        else :
            newPrimes.append(i)
        i = i + 1
    lastPrime = len(primes)
    primes = newPrimes

    for j in range(3, lastPrime):
        if (primes[j] != 0):
            k = math.floor(lastPrime/j) + 1
            mul = j*k
            while (mul < n):
                primes[mul] = 0
                k = k + 1
                mul = j*k
    return primes

primes = [0, 1, 2, 3, 0, 5, 0, 7, 0, 0, 0]
