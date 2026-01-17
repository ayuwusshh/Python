n=abs(int(input()))
while n>=10:
  if n%2==0:
    s=0
    temp=n
    while temp>0:
      s+=temp%10
      temp//=10
    n=s
  else:
    p=1
    temp=n
    while temp>0:
      p*=temp%10
      temp//=10
    n=p
print(n)