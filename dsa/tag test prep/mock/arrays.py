#generate permutaions
# def backtrack(a,b,c,path):
#   if a==0 and b==0 and c==0:
#     print("".join(path))
#     return
#   if a>0:
#     backtrack(a-1,b,c,path+['a'])
#   if b>0:
#     backtrack(a,b-1,c,path+['b'])
#   if c>0:
#     backtrack(a,b,c-1,path+['c'])
# n1,n2,n3=map(int,input().split())
# backtrack(n1,n3,n3,[])

#Problem

'''
You are given an integer array arr of size N and an integer K.
Find the length of the longest contiguous subarray such that:
(max element – min element) ≤ K
Input
N = 6
arr = [8, 2, 4, 7, 6, 5]
K = 4
Output  4

'''
# n=int(input())
# arr=list(map(int,input().split()))
# k=int(input())
# count=0
# mx=0
# for i in range(len(arr)):
#   while max(arr[count:i+1])-min(arr[count:i+1])>k:
#     count+=1
#   mx=max(count,i-count+1)
# print(mx)
# n=int(input())
# arr=list(map(int,input().split()))
# k=int(input())
# n=len(arr)
# ans=[]
# mx=0
# for i in range(n):
#   for j in range(i,n):
#     ans.append(arr[i:j+1])
# for word in range(len(ans)):
#   if max(ans[word])-min(ans[word])<=k:
#     mx=max(mx,len(ans[word]))
# print(mx)

'''

You are given an array of size N.
In one operation, you can remove either the first or the last element.
Find the minimum number of operations required to make the array sorted in non-decreasing order.

Input
N = 5
arr = [3, 1, 2, 4, 5]

Output
1
'''

# arr = list(map(int, input().split()))
# n = len(arr)
# #7 2 3 1 2 4 5 9
# max_len = 1
# curr_len = 1

# for i in range(1, n):
#     if arr[i] >= arr[i-1]:
#         curr_len += 1
#         max_len = max(max_len, curr_len)
#     else:
#         curr_len = 1
# deletions = n - max_len
# print(deletions)

'''
Given a binary array, count the number of subarrays with equal number of 0s and 1s.
Input 6 0 0 1 0 1 1
Output: 5
'''
# from collections import Counter
# from itertools import accumulate
# from math import comb
# arr=list(map(int,input().split()))
# arr=[-1 if x==0 else 1 for x in arr]
# prefix=list(accumulate(arr))
# freq=Counter(prefix)
# ans=freq[0]
# for i in freq.values():
#   ans+=comb(i,2)
# print(ans)

#Q4. Maximum Sum Subarray After One Deletion
'''
You can delete at most one element. Find the maximum subarray sum.
Input
5
1 -2 0 3
Output  4
'''
# arr = [1, -2, 0, 3]
# n=len(arr)
# sub = []
# sub_sum = []
# for a in range(n):
#     temp=[]
#     for b in range(a,n):
#         temp=arr[a:b+1]
#         sub.append(temp)
#         sub_sum.append(sum(temp))
# res=max(sub_sum)
# for a in range(len(sub)):
#     if((sub_sum[a]-min(sub[a]))> res):
#         res = sub_sum[a]-min(sub[a])
# print(res)
