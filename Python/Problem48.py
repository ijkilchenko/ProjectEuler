import math

s = 0

for i in range(1, 1001):
    num = 1
    for j in range(1, i+1):
        num = num*i % math.pow(10,10)
    s = (s + num) % math.pow(10,10)

print(s)
