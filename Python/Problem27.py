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
    count = 0
    """
    for j in range(0, len(primes)):
        if (primes[j] != 0) :
            count = count + 1
    print(count - 1)
    """
    return primes

primes = [0, 1, 2, 3, 0, 5, 0, 7, 0, 0, 0]
#print(isPrime(15485863)) #Should print 'True'

def quadratic(a, b, n) :
    return math.pow(n, 2) + a *n + b

def getLengthOfPrimes(a, b) :
    n = 0
    num = quadratic(a, b, n)
    while (isPrime(round(num))):
        n = n + 1
        num = quadratic(a, b, n)
    return n

def getBestQuadratic() :
    bestA = 0
    bestB = 0
    bestLen = 0
    for b in range(-999, 1000) :
        for a in range(-999, 1000) :
            currentLen = getLengthOfPrimes(a, b)
            if (currentLen > bestLen):
                bestLen = currentLen
                bestA = a
                bestB = b
    print(bestLen)
    print(bestA)
    print(bestB)
    print(bestA * bestB)

getBestQuadratic()
