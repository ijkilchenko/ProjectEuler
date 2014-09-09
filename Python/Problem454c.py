"""
Project Euler Problem 454
"""
# grab functions from my Project Euler 454 library module
from E454tools import factorize, divisors_from_factors
import time

# set initial conditions, including count of solutions, y and y**2
# y is the only required input

count = 0
y = 100
y_sq = y**2  # square the value for y
starttime = time.time()

# next we're going to get a list of divisors of y**2 from its prime factorization

# first we factorize y_sq using divisors from factors function
# next, we produce a list of divisors using divisors from factors function
# finally, we assign the result to list_of_divisors_of_y_sq variable

list_of_divisors_of_y_sq = divisors_from_factors(factorize(y_sq))

# then we're going to throw out the high and low value (1 and y**2)
# we don't need these two values because n < x < y

del list_of_divisors_of_y_sq[0], list_of_divisors_of_y_sq[-1]

# this for loop looks at each divisor in list_of_divisors_of_y_sq

for divisor in list_of_divisors_of_y_sq:

    # set the value for x
    x = divisor - y

    # test if the inequality is true
    # if it passes, print out the result
    if 0 < x < y:

        print "y =", y, "n =", (x*y)/(x + y), "x =", x
        print "divisor", divisor

        # add one to the count
        count += 1

# at for loop termination, print the total count
print "Found", count, "solutions in", time.time() - starttime, "seconds"


"""


starttime = time.time()
sequence = A005279()
y = sequence.next()


print "-----------------------------------"

count = 0

while y < 10**9+1:
    y_sq = y**2
    divisors1 = divisors_from_factors(factorize(y_sq))
    del divisors1[0], divisors1[-1]
    for divisora in divisors1:
            if 0 < divisora - y < y:
                # print ">>> solution at x =", (divisora - y)
                count += 1
    y = sequence.next()
    if count % 10000 == 0:
        print "counting .... currently at", y
print "Stopped at", y, " and found", count, "solutions in", time.time() - starttime, "seconds"


"""
