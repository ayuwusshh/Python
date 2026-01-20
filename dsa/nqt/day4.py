#1
# num=list(map(int,input().split()))
# # 1 2 3 6 4
# add=0
# ans=-1
# for i in range(len(num)):
#   if num[i]==add:
#     ans=num[i]
#     break
#   else:
#     add+=num[i]
# print(ans)

#2
# num=list(map(int,input().split()))
# ans=-1
# total=sum(num)
# left=0
# for idx in range(len(num)):
#   right=total-left-num[idx]
#   if left==right:
#     ans=idx
#     break
#   else:
#     left+=num[idx]
# print(ans)

#3
# s=input()
# ans=-1
# freq={}
# for ch in s:
#   freq[ch]=freq.get(ch,0)+1
# for ch in s:
#   if freq[ch]==2:
#     ans=ch
#     break
# print(ans)

#4
s=input()   # a b a b
n=len(s)
ans=-1
for i in range(1,n):
  prefix=s[:i]
  suffix=s[n-i:]
  if prefix==suffix:
    ans=prefix
print(ans)

#5
# num=list(map(int,input().split()))
# total=sum(num)
# left=0
# ans=-1
# for i in range(len(num)):
#   right=total-left-num[i]
#   if left>right:
#     ans=num[i]
#     break
#   else:
#     left+=num[i]
# print(ans)