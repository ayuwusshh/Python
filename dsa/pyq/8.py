n=int(input())
add=0
for i in range(1,n+1):
  add+=i
if add%9==0:
  print('Yes')
else:
  print('No')