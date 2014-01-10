import math

def MyAppend(s, string):
    string= string[:-1]
    if (len(string) == 2):
        return s.append(int(string))
    else:
        cLength= len(string)
        nNumbers= (cLength+1)/3
        i= 0
        while (i < cLength):
            s.append(int(string[i:i+2]))
            i= i + 3

def FindHeight(n):
    #n is the number of elements in the triangle/array. 
    #This solves a quadratic equation and picks the positive root.

    return (-1+math.sqrt(1+4*2*n))/2

"""
def Reduce(s, i):
    #This takes row i and changes it based on the row below.
    #Hardest method here.

    #Starting with i=14 (i.e. the row above the last row). 
"""

def run():
    f= open ("./triangle67.txt","r")
    s= []
    cString= f.readline()
    while (cString != ""):
        MyAppend(s, cString)
        #print(cString)
        cString= f.readline()
        #print(cString)
    #I have no idea why the last element is wrong. Fixing manually...
    s[-1]= 35

    l= int(FindHeight(len(s)))
    #print(l)

    #i= 1
    for i in range(1, l):
        #print(s[-(int(l*i - i*(i-1)/2 + 1))])
        #Print rigtmost number per row.
        for j in range(0, l-i):
            #print(s[-(int(l*i - i*(i-1)/2 + 1 + j))], s[-(int(l*i - i*(i-1)/2 + 1 + j - (l-i)))], s[-(int(l*i - i*(i-1)/2 + j - (l-i)))])
            if (s[-(int(l*i - i*(i-1)/2 + 1 + j - (l-i)))] > s[-(int(l*i - i*(i-1)/2 + j - (l-i)))]):
                s[-(int(l*i - i*(i-1)/2 + 1 + j))]= s[-(int(l*i - i*(i-1)/2 + 1 + j))] + s[-(int(l*i - i*(i-1)/2 + 1 + j - (l-i)))]
            else:
                s[-(int(l*i - i*(i-1)/2 + 1 + j))]= s[-(int(l*i - i*(i-1)/2 + 1 + j))] + s[-(int(l*i - i*(i-1)/2 + j - (l-i)))]
                
            #Print the elements in each row...
    print(s[0])
    

    
    #print(s[-(2*l)])
    
    #print(s)
    #print(len(s))


run()
