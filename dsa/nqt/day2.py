# 1--> Balanced String Check
# from collections import Counter
# s=input()
# ac=0
# bc=0
# freq={}
# freq=Counter(s)
# for ch in s:
#   if ch=='a':
#     ac=freq[ch]
#   else:
#     bc=freq[ch]
# if ac==bc:
#   print('YES')
# else:
#   print('NO')

# 2--> Array Rotation by K (Right Rotation)
# num=list(map(int,input().split()))
# n=len(num)
# k=int(input())
# k=k%n
# arr=[]
# ans=[]
# for i in range(n-2,n):
#   arr.append(num[i])
# for idx in arr:
#   ans.append(idx)
# for i in range(n-k-1):
#   ans.append(num[i])
# print(ans)

#3-->First Non-Repeating Character
# s=input()
# freq={}
# for ch in s:
#   freq[ch]=freq.get(ch,0)+1
# ok=False
# ans=''
# for ch in s:
#   if freq[ch]==1:
#     ok=True
#     ans=ch
#     break
# if ok:
#   print(ans)
# else:
#   print('-1')

#4--> Longest Increasing CONTIGUOUS Subarray
# num=list(map(int,input().split()))
# ans=0
# curr_len=0
# max_len=0
# for i in range(1,len(num)):
#   if num[i]>num[i-1]:
#     curr_len+=1
#     max_len=max(curr_len,max_len)
#   else:
#     curr_len=1
# print(max_len)

#5--> Count Numbers Divisible by BOTH 3 and 5
# num=list(map(int,input().split()))
# count=0
# for val in num:
#   if val%15==0:
#     count+=1
# print(count)

#6--> Digital Root
# n=int(input())
# while n>=10:  # 9999
#   temp=n  # 9999
#   add=0 #
#   while temp>0: # 9
#     add+=temp%10  # 36
#     temp//=10 # 9
#   n=add
# print(n)

#7-–> Count Pairs with Given Sum

# from itertools import combinations
# num=list(map(int,input().split()))
# k=int(input())
# ans=0
# for a,b in combinations(num,2):
#   if a+b==k:
#     ans+=1
# print(ans)

#8--> Remove Adjacent Duplicates
# s=input()
# ans=s[0]
# for ch in range(1,len(s)):
#   if s[ch]==ans[-1]:
#     continue
#   else:
#     ans+=s[ch]
# print(ans)

#9-–> Check Armstrong Number
# n=int(input())
# prev=n
# res=0
# while n>0:
#   d=n%10
#   res+=d*d*d
#   n//=10
# if prev==res:
#   print("YES")
# else:
#   print("NO")

#10–-> Majority Element
# num=list(map(int,input().split()))
# n=len(num)
# t=n/2
# freq={}
# for i in num:
#   freq[i]=freq.get(i,0)+1
#ans=-1
# for val in num:
#   if freq[val]>t:
#     print(val)
#     ans=val
#     break
# print(ans)

#11--> Check Rotation
# s1=input()
# s2=input()
# if len(s1)==len(s2) and s2 in s1+s2:
#   print("YES")
# else:
#   print("NO")