def run():
    n= 0
    i= 0
    while (n <= 10):
        n= math.floor(math.log(55,10)+i*math.log(1.61803398875,10))
        i= i+1
    print(i-1)
    
run()
