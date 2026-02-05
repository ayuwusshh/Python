import math
def isPrime(n):
 return n>1 and all(n%i for i in range(2,int(n**0.5)+1))
def isSquare(n):
 return int(math.sqrt(n))**2==n
def nthTerm(N):
 series=[0]*(N+1)
 p2=0
 p3=0
 for i in range(1,N+1):
  if isPrime(i):
   series[i]=2**(p2)
   p2+=1
  elif isSquare(i):
   series[i]=3**(p3)
   p3+=1
  else:
    series[i]=series[i-1]+series[i-2]
 return series[N]
n=int(input())
print(nthTerm(n))