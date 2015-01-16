import utilsPrimes as utils

def solve():
    condition = False
    i = 1
    f = []
    f.append(utils.getPrimeFactors(i))
    f.append(utils.getPrimeFactors(i + 1))
    f.append(utils.getPrimeFactors(i + 2))
    f.append(utils.getPrimeFactors(i + 3))
    i = i + 1
    while (condition == False):
        f[0] = f[1]
        f[1] = f[2]
        f[2] = f[3]
        f[3] = utils.getPrimeFactors(i + 3)
        flag = False
        if (len(f[0]) == 4 and len(f[1]) == 4 and len(f[2]) == 4 and len(f[3]) == 4):
            for k in range(0, len(f) - 1):
                flag = False
                h = {}
                for j in f[k].keys():
                    F = j
                    try:
                        if (h[F] == 1):
                            flag = False
                            break
                    except KeyError:
                        flag = True
                        h[F] = 1
                if (flag == False):
                    break
                k = k + 1
                for j in f[k].keys():
                    F = j
                    try:
                        if (h[F] == 1):
                            flag = False
                            break
                    except KeyError:
                        flag = True
                        h[F] = 1
                if (flag == False):
                    break
                k = k - 1
        if (flag == True):
            condition = True
        else:
            i = i + 1
    return i

print(solve())
            
                
