m=int(input())
nums=list(map(int,input().split()))
mx=[]
n=len(nums)
freq={}
for i in nums:
  freq[i]=freq.get(i,0)+1
for key,value in freq.items():
  if value>=n//2:
    mx.append(key)
print(mx)
