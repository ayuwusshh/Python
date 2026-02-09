n1,n2=map(int,input().split())
ans=[]
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(n1,n2+1):
  if isPrime(i):
    digit=i
    res=i
    summ=0
    while digit>0:
      summ+=digit%10
      digit//=10
    if isPrime(summ):
      ans.append(res)
print(ans)