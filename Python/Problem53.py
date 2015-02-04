import math

def solve():
    count = 0
    for n in range(1, 101):
        for r in range(0, n+1):
            comb = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
            if (comb > 1000000):
                count = count + 1
    print(count)

solve()
