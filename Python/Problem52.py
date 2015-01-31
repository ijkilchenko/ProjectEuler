import utilsPandigitals as u

def solve():
    i = 1
    while(True):
        for j in range(2, 7):
            if (u.isPermutation(str(i*j), str(i))):
                if (j == 6):
                    print(i)
                    return
                continue
            else :
                break
        i = i + 1
        #print(i)

solve()
