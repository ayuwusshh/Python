#Q1. Minimum Penalty Shop Problem 
'''A shop is open for n hours.
You are given a string of Y and N.
Rules:
Shop open & no customer (N) → penalty +1
Shop closed & customer comes (Y) → penalty +1
Find the earliest hour to close shop with minimum penalty.
Input:YYNY Output:2'''
# s=input()
# n=len(s)
# minn=float('inf')
# i=0
# ans=0
# while i<=n:
#   penalty=0
#   j=0
#   #left check
#   while j<i:
#     if s[j]=='N':
#       penalty+=1
#     j+=1
#   #right check
#   j=i
#   while j<n:
#     if s[j]=='Y':
#       penalty+=1
#     j+=1
#   if penalty<minn:
#     minn=penalty
#     ans=i
#   i+=1
# print(ans)


#Q2. Array Reduction Game

'''
Given an array, repeat until size becomes 1:
Pick any two adjacent elements
Replace them with their absolute difference
Find the minimum possible final value.
Input:4 
      1 2 3 4    Output:0
'''
# n=int(input())
# arr=list(map(int,input().split()))
# while len(arr)>1:
#   new_arr=[]
#   for i in range(len(arr)-1):
#      new_arr.append(abs(arr[i] - arr[i + 1]))
#   arr=new_arr
# print(arr[0])

#Q3. Maximum Sum Subarray (Classic but Important)

'''
Given an array of integers, find the maximum sum of a contiguous subarray.
Input: 8 -> -2 -3 4 -1 -2 1 5 -3
Output: 7
'''
# n=int(input())
# nums=list(map(int,input().split()))
# mx=nums[0]
# summ=nums[0]
# for i in range(1,n):
#   summ=max(nums[i],summ+nums[i])
#   mx=max(summ,mx)
# print(mx)

#Q4. First Non-Repeating Character
'''
Given a string, print the first character that does not repeat.
Input: swiss
Output: w
'''
# s=input()
# n=len(s)
# freq={}
# for i in s:
#   freq[i]=freq.get(i,0)+1 #{'s': 3, 'w': 1, 'i': 1}
# for i in s:
#   if freq[i]==1:
#     print(i)
#     break

#Q5. Rotation + Condition (Twist Question)
'''
Two strings are given. Print Yes if:
One is rotation of the other
AND they contain exactly 2 vowels
Input:abcde cdeab
Output: Yes
'''
# s1,s2=input().split()
# def rotation(s1,s2):
#  return len(s1)==len(s2) and s2 in (s1+s1)

# s1even=0
# s2even=0
# for ch in s1:
#   if ch in 'aeiou' or ch in 'AEIOU':
#     s1even+=1
# for ch in s2:
#   if ch in 'aeiou' or ch in 'AEIOU':
#     s2even+=1
# if s1even==2 and s2even==2 and rotation(s1,s2):
#   print("Yes")
# else:
#   print("No")

'''
Q6.Minimum Absolute Difference

Given N numbers, find minimum absolute difference between any two elements.
Input:
5
3 8 15 17 9
Output:1
'''

# n=int(input())
# nums=list(map(int,input().split()))
# minn = float('inf')
# for i in range(len(nums)-1):
#   for j in range(i+1,len(nums)):
#     diff=abs(nums[j]-nums[i])
#     minn=min(minn,diff)
# print(minn)


#Q7. Bus Allocation Problem (Greedy)

'''
You have N students and each bus can carry K students.Find minimum number of buses required.
Input:57 10
Output:6
'''
n,m=map(int,input().split())
if n%10==0:
  print(n//m)
else:
  print((n//m) +1)