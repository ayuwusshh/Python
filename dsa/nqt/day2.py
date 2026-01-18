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