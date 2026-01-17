
n=int(input())
nums=list(map(int,input().split()))
minn=nums[0]
for i in range(len(nums)-1):
  for j in range(i+1,len(nums)):
    diff=abs(nums[j]-nums[i])
    minn=min(minn,diff)
print(minn)
