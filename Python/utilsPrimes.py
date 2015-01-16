import math
import copy

primes = [2, 3, 5, 7]

def isPrime(n) :
    global primes
    if (n < 2) :
        return False
    else:
        if (n != 2 and n % 2 == 0):
            return False
        else:                
            if (math.floor(n/2) < len(primes)) :
                if (primes[math.floor(n/2)] == 0) :
                    return False
                else:
                    return True
            else:
                primes = getPrimes(primes)
                return isPrime(n)
factors = {}

def getPrimeFactors(n):
    if (n == 1):
        return
    else:
        num = n
        try:
            return factors[num]
        except KeyError:
            if (isPrime(n)):
                return {n : 1}
            i = 2
            while (n%i != 0):
                if (i == 2):
                    i = i + 1
                else:
                    i = i + 2
            n = n/i
            ff = copy.deepcopy(getPrimeFactors(n))
            
            try:
                if (ff[i] > 0):
                    count = ff[i]
                    ff[i] = count + 1
            except KeyError:
                ff[i] = 1
                
            factors[num] = ff
            return factors[num]

def getPrimes(primes):
    n = 2*len(primes)
    lastPrime = math.floor(2*len(primes)) - 1
    i = lastPrime + 2
    while (i < 2*n):
        if (i % 2 == 0):
            i = i + 1
        else :
            primes.append(i)
            i = i + 2

    for j in range(1, lastPrime):
        if (primes[j] != 0):
            k = math.floor(lastPrime/primes[j]) + 1
            if (k % 2 == 0):
                k = k + 1
            if (primes[j] > k):
                k = primes[j]
            mul = primes[j]*k
            while (mul < 2*n):
                primes[math.floor(mul/2)] = 0
                k = k + 2
                mul = primes[j]*k
    return primes
