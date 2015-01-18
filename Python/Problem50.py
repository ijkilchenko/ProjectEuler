import utilsPrimes as u

def solve():
    bestL = 0
    bestP = 0
    p = 2
    length = 2
    bound = 1000000
    while (p < bound): 
        s = 0
        last = p
        length = 2
        while (s < bound):
            s = s + last
            last = u.nextPrime(last)
            if (u.isPrime(s) and length > bestL):
                bestL = length
                bestP = s
                if (bestP > bound):
                    break
                else:
                    print(p, bestL, bestP)
            length = length + 1
        p = u.nextPrime(p)
        
    print(bestL, bestP)

solve()
