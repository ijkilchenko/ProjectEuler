import utilsPrimes as p
import utilsPandigitals as l

def solve():

    i = 1001
    while (i < 9999):
        if (p.isPrime(i)):
            ll = l.getListOfPermutations(str(i))
            diff = 0
            num = 0
            for n in ll:
                num = int(n)
                if (num != i and p.isPrime(num)):
                    diff = num - i
                    last = num + diff
                    try:
                        if (ll.index(str(last)) >= 0 and p.isPrime(last)):
                            print(i, num, last)
                    except ValueError:
                        continue
                    
        i = i + 2

solve()
        

    
