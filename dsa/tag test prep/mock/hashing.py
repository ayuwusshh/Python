#Subarray Sum Equals K
'''
Count number of subarrays whose sum equals K.
Input:
5
1 2 3 -2 5
3
Output:3
'''
# n=int(input())
# nums=list(map(int,input().split()))
# k=int(input())
# freq=0
# subarray=[]
# for i in range(len(nums)):
#   for j in range(i,len(nums)):
#     subarray.append(nums[i:j+1])
# for ans in subarray:
#   if(sum(ans)==k):
#     freq+=1
# print(subarray)
# print(freq)


#2nd attempt
# n=int(input())
# nums=list(map(int,input().split()))
# k=int(input())
# freq=0
# for i in range(len(nums)):
#   for j in range(i,len(nums)):
#    val= sum(nums[i:j+1])
#    if val==k:
#      freq+=1
# print(freq)



#. Pair With Given Difference
'''
Check if there exists a pair such that:
arr[i] - arr[j] = K
Input:
5
5 20 3 2 50
17
Output: Yes
'''

n=int(input())
nums=list(map(int,input().split()))
k=int(input())
ans=0
res=False
for i in range(len(nums)):
  for j in range(len(nums)):
    val=nums[i]-nums[j]
    if val==k:
      res=True
      break
  if res:
    break
if res:
  print('Yes')
else:
  print('No')
