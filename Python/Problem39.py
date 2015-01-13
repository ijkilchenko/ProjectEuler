def solve():
    bestP = 120
    bestCount = 3
    for p in range(12, 1001):
        count = 0
        for a in range(1, p - 1):
            for b in range(1, p - a):
                c = p - a - b
                if (c**2 == a**2 + b**2):
                    count = count + 1
        if (count > bestCount):
            bestCount = count
            bestP = p
            print(bestP, bestCount)
    print(bestP, bestCount)

solve()
