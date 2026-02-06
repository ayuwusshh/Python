num=list(map(int,input().split())) # 2 4 7 1 6 3
k=int(input())  #3
ans=[]
j=k-1
i=0
while j<len(num):
  ans.append(max(num[i:j+1]))
  j+=1
  i+=1
print(ans)