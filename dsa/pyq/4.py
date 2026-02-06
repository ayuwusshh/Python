n=int(input())
fibo=[]
fibo.append(0)
fibo.append(1)
fibo.append(1)
for i in range(3,n):
  fibo.append(fibo[i-1]+fibo[i-2])
print(sum(fibo))
