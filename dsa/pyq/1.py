num=list(map(int,input().split()))
t=int(input("Enter target: "))
n=len(num)
ans=[]
for i in range(n):
  res=0
  for j in range(i,n):
    res+=num[j]
    if res==t:
      ans.append(num[i:j+1])
print(ans)