import utilsPrimes as utils

import math

def solve():
    conjecture = True
    n = 9
    while (conjecture == True):
        conjecture = False
        while (utils.isPrime(n)):
            n = n + 2
        for i in range(2, n - 1):
            if (utils.isPrime(i)):
                twice = n - i
                j = 1
                difference = twice - 2*j**2
                while (difference >= 0):
                    if (difference == 0):
                        conjecture = True
                        print(n, '=', i, '+2*', j, '^2')
                        break
                    j = j + 1
                    difference = twice - 2*j**2
                if (conjecture == True):
                    break
        if (conjecture == False):
            return n
        n = n + 2

print(solve())
            
                
                    
