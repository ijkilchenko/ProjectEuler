import utilsPrimes as utils
import math
import time

'''
start = time.time()
print(utils.isPrime(13))
print(utils.isPrime(23))
print(utils.isPrime(14))
print(utils.isPrime(25))
print(utils.isPrime(15485867))
print(utils.isPrime(15485))
print(utils.isPrime(15485867))
print(utils.isPrime(15485865))
end = time.time()
print(end - start)
'''

'''
i = 2
while (i < 10000):
    f = utils.getPrimeFactors(i)
    n = 1
    for j in f.keys():
        n = n * j**f[j]
    if (i != n):
        print(i, n, f)
    i = i + 1

'''
print(utils.getPrimeFactors(9))
print(utils.getPrimeFactors(27))
print(utils.getPrimeFactors(27))
print(utils.getPrimeFactors(9))
