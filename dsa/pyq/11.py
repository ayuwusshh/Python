n=int(input())
nums=list(map(int,input().split()))
nums.sort()
case1=nums[-1]*nums[-2]*nums[-3]
case2=nums[0]*nums[1]*nums[-1]
print(max(case1,case2))