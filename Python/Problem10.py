import math

def run():

    numbersL= [i for i in range(1, int(2*math.pow(10,2)+1))]
    currentP= numbersL[1]

    #print(numbersL)
    #print(currentP)
    #print(len(numbersL))

    while (currentP <= len(numbersL)):
        i= 2
        while (currentP*i <= len(numbersL)):
            numbersL[currentP*i-1]= 0
            i= i+1
        j= 1
        if (currentP + j >= len(numbersL)):
            break
        while (numbersL[currentP + j -1] == 0):
            j= j+1
            if (currentP + j >= len(numbersL)):
                break
        currentP= currentP + j
        #print(currentP)

        
        
    #print(numbersL)
    #print(currentP)
    print(numbersL)
    print(sum(numbersL)-1)
    
        

run()
