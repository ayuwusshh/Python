n=input().strip()
r=int(input())
if r==0:
  print('0')
  exit()
s=sum(int(d) for d in n)*r
print(9 if s%9==0 else s%9)