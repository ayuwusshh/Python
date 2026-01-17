#2
# s=input()
# ans=''
# i=0
# while i in range(len(s)):
#   ans+=s[i]
#   i+=2
# print(ans)

#3
# num=list(map(int,input().split()))
# n=len(num)
# ans=0
# for i in num:
#   if i<=1:
#     ans+=i*i*i
#     cotinue
#   isprime=True
#   for j in range(2,i):
#     if i%j==0:
#       isprime=False
#       break
#   if isprime:
#     ans+=i*i
#   else:
#     ans+=i*i*i
# print(ans)

#4
# from collections import Counter
# s=input()
# freq={}
# freq=Counter(s)
# print(freq)
# ans=''
# mx=0
# for ch in s:
#   if freq[ch]>mx:
#     mx=freq[ch]
#     ans=ch
# print(ans)

#5
from itertools import combinations
num=list(map(int,input().split()))
l=0
unique=set()
for i in range(1,len(num)+1):
  unique.update(combinations(num,i))
for word in unique:
  if list(word)==sorted(word) and len(set(word))==len(sorted(word)):
    l=max(l,len(word))
print(len(num)-l)