n=list(map(int,input().split()))
ans=0
# 2 4 5 6
for i in n:
  if i<=1:
    ans+=i*i*i
  else:
    is_prime=True
    for j in range(2,i):
      if i%j==0:
        is_prime=False
        break
    if is_prime:
      ans+=i*i
    else:
      ans+=i*i*i
print(ans)