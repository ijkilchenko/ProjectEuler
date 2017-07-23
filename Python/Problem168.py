A=[9,19,29,39,49,59,69,79,89]
X=[]
for N in range(1,100):
  for i in range(1,10):
    for a in A:
      if i*(10**(N+1)-1) % a == 0:
        x=i*(10**(N+1)-1) / a
        if len(str(x)) == N + 1:
          X.append(x)
print(str(sum(X))[-5:])
