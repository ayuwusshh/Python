#Problem: Digit Frequency Check

'''
Given a number N, check whether all digits occur the same number of times.
Input:1212
Output:Yes
Explanation:Digits 1 and 2 → both occur 2 times
'''
# inp=input()
# arr=[]
# for ch in inp:
#   arr.append(ch)
# freq={}
# for i in arr:
#   freq[i]=freq.get(i,0)+1
# values=list(freq.values())
# same=True
# for i in range(1,len(values)):
#   if values[i]!=values[0]:
#     same=False
#     break
# if same:
#   print('Yes')
# else:
#   print('No')

#QUESTION 2 –  Problem: Array Leader Elements
'''
An element is a leader if it is greater than all elements to its right.
Print all leaders in the order they appear.
Input:6 -> 16 17 4 3 5 2
            i j
Output: 17 5 2
'''
# n=int(input())
# nums=list(map(int,input().split()))
# arr=[]
# i=0
# while i < n:
#   j=i+1
#   while j<n:
#     if nums[j]>nums[i]:
#       break
#     j+=1
#   else:
#     arr.append(nums[i])
#   i+=1
# print(arr)

#QUESTION 3 – Electricity Bill Calculation
'''
Rules: First 100 units → ₹5/unit Next 100 units → ₹7/unit 
Above 200 units → ₹10/unit
Input:250 Output:1750
'''
# n=int(input())
# if n<=100:
#   print(n*5)
# elif n<=200:
#   print(100*5+(n-100)*7)
# else:
#   print((100*5+100*7)+(n-200)*10)

#QUESTION 4 – Longest Word Finder
'''
Given a sentence, print the longest word. If multiple, print the first one.
Input:  TCS is hiring fresh engineers
Output: engineers
'''
# s=input()
# arr=s.split()
# length=[]
# for i in arr:
#   length.append(len(i))
# idx=length.index(max(length))
# print(length)
# print(arr[idx])


#QUESTION 5 – Valid Mountain Array
'''
An array is a mountain array if:
Strictly increasing
Then strictly decreasing
At least 3 elements
Input:
5
0 3 5 4 1
Output:Yes
'''
n=int(input())
arr=list(map(int,input().split()))
length=len(arr)
if length<3:
  print('No')
idx=arr.index(max(arr))
ok=True
i=0
while i<idx:
  if arr[i]>=arr[idx]:
    ok=False
  i+=1
i=idx+1
while i<len(arr):
  if arr[i]>=arr[idx]:
    ok=False
  i+=1
if ok:
  print('Yes')
else:
  print('No')