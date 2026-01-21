# 1
# num=list(map(int,input().split()))
# ans=-1
# n=len(num)
# total=sum(num)
# left=0
# for i in range(len(num)):
#   right=total-left-num[i]
#   if left>right:
#     val=num[i]
#     s=str(abs(val))
#     if s==s[::-1]:
#       ans=val
#     break
#   left+=num[i]
# print(ans)

#2
# num=list(map(int,input().split()))
# ans=-1
# n=len(num)
# for i in range(n):
#   befok=True
#   aftok=True
#   for x in num[:i]:
#     if x>=num[i]:
#       befok=False
#       break
#   for x in num[i+1:]:
#     if x<=num[i]:
#       aftok=False
#       break
#   if befok and aftok:
#     ans=num[i]
#     break
# print(ans)  

#3
# s=input()
# freq={}
# ans=-1
# for ch in s:
#   freq[ch]=freq.get(ch,0)+1
# for i in range(1,len(s)):
#   if freq[s[i]]==1 and s[i-1] in 'aeiou':
#     ans=s[i]
#     break
# print(ans)

#4
# num=list(map(int,input().split()))
# n=len(num)
# ans=-1
# if n==0:
#   print(ans)
# else:
#   avg=sum(num)/n
#   for val in num:
#     if val%2==0 and val>avg and val%4!=0:
#       ans=val
#       break
#   print(ans)