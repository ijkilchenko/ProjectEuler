def Num2Word(n):
    #num= str(n)
    #The following could be implemented using a dictionary.

    return {
        '1': "one",
        '2': "two",
        '3': "three",
        '4': "four",
        '5': "five",
        '6': "six",
        '7': "seven",
        '8': "eight",
        '9': "nine",
        '10': "ten",
        '11': "eleven",
        '12': "twelve",
        '13': "thirteen",
        '14': "fourteen",
        '15': "fifteen",
        '16': "sixteen",
        '17': "seventeen",
        '18': "eighteen",
        '19': "nineteen",
        '0': "",
        }.get(n)

def Numb2Word(n):
    #num= str(n)
    #The following could be implemented using a dictionary.

    first= {
        #'1': "one",
        '2': "twenty",
        '3': "thirty",
        '4': "forty",
        '5': "fifty",
        '6': "sixty",
        '7': "seventy",
        '8': "eighty",
        '9': "ninety",
        '0': "",
        }.get(n[0])
    second= Num2Word(n[1])
    return first+second

def Numbe2Word(n):

    second= "hundred"
    #print(int(n[1:]))
    if (len(n[1:]) <= 2 and int(n[1:]) <= 20 and int(n[1:]) != 0):
        if (int(n[1]) == 0):
            #print(Num2Word(n[2:]))
            second= "hundredand" + Num2Word(n[2:])
        if (int(n[1]) == 1):
            Num2Word(n[1:])
            second= "hundredand" + Num2Word(n[1:])
    if (len(n[1:]) == 2 and int(n[1]) >= 2):
        second= "hundredand" + Numb2Word(n[1:])
    
    return Num2Word(n[0])+second

def Number2Word(n):
    num= str(n)

    if (int(num) == 1000):
        return "onethousand"
    if (len(n) <= 2 and (int(num[0]) == 1 or len(n) == 1)):
        return Num2Word(n)
    if (len(n) == 2 and int(num[0]) >= 2):
        return Numb2Word(n)
    if (len(n) == 3):
        return Numbe2Word(n)
        
    
def run():
    #print(len(Number2Word("999")))

    #f = open('./problem17output.txt', 'w')
    total= 0
    for i in range (1, 1001):
        number= Number2Word(str(i))
        total= total+ len(number)
        #print(i, number)
        #f.write(str(str(i) + " " + number + "\n"))
    print(total)    
    

#print(Number2Word("2"))
run()
