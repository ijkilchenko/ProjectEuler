"""
Author: Alexey Ilchenko.

Below is my solution to Project Euler problem #16 (the problem can be found at
http://projecteuler.net/problem=16) written in Python 3. 

Problem statement: What is the sum of the digits of the number 2^(1000)?

My solution/discussion: The naive approach which is used by many people is
simply to calculate 2^(1000) and then convert to string and add all the digits.
So, a naive solution in Python is:

sum = 0
for n in str(2**1000):
	sum += int(n)
print sum

I recognized this approach right away and decided that it was not in spirit of
the problem. One reason is because you may not be able to store 2^(1000) as a
variable on a computer; you would need about 1000 bits to store such a number.
Without using some special library, I decided to make my own algorithm that
would not be dependent on storing big numbers. 

The space complexity is not 2^(1000) anymore, but is only two vectors of length
1000 (which are continuously rewritten and swapped).  
"""

import math

def run():

    n= 1000 #This is the exponent on the 2. Ex: 2^n=2^1000. 
    N= n+ 1 #I use a different variable N=n+1 for convenience. 

    """
    x is a vector of powers of 2 with only the first digit kept.
    Ex: [2 4 8 16 32] -> [2 4 8 6 2]
    """
    x= [math.pow(2,i)%10 for i in range(1,N)]
    """
    y is a vector reserved for the second digits to be calculated later.
    (y is all 0's at first.) 
    Ex: y= [0 0 0 1 3] after we only keep the first digits in our x vector. 
    """
    y= [0 for i in range(1,N)]
    
    total= x[len(x)-1] #This is the sum of the digits so far. 

    #The range of the for-loop is dependent on the "length" of the number 2^n.
    for j in range(1,math.floor(N*math.log(2,10))+1):
        y= [0 for i in range(1,N)]
        for i in range(1,N-1):
            #This is the key idea of the algorithm! 
            #We calculate each digit of 2^n separately per j-loop iteration
            #and only store the vectors needed to calculate for the next
            #iteration. 
            y[i]= math.floor(((y[i-1]*10+x[i-1])*2)/10)%10
        x= y #Vectors are reused for space efficiency. 

        total= total + y[len(y)-1] #Next digit is added to the sum of digits. 

    print("The answer using the 'harder' approach is", int(total))

    sum= 0
    for n in str(2**n):
        sum += int(n)
    print("The answer using the 'naive' approach is", sum)
 
run()

"""
Conclusion: I believe that my approach to this rather simple problem
quickly illustrates my education in terms of both mathematics and computer science.
I was able to recognize the limitations of a naive algorithm and I built an
interesting algorithm which is scalable (in terms of space complexity) and
is independent of the aforementioned storage limitation. 

Please, email me at axi48@case.edu for any further explanations. 
"""
