"""
Author: Alexey Ilchenko
Problem 1 of Project Euler
"""
def run():
    total= 0
    for i in range (1, 1000):
        if (i%3==0 or i%5==0):
            total= total + i
    print(total)
    
run()
