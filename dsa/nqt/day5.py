#1
# num=list(map(int,input().split()))
# s=input()
# ans=-1
# total=sum(num)
# left=0
# for i in range(len(num)):
#   right=total-left-num[i]
#   if right==left:
#     if i<len(s):
#       ans=s[i]
#     else:
#      ans=-1
#     break
#   left+=num[i]
#print(ans)

#2
# s=input()
# n=len(s)
# ans=-1
# for i in range(n):    #a b c b a
#   left=i
#   right=n-i-1
#   if right==left:
#     ans=s[i]
#     break
# print(ans)

#3
num=list(map(int,input().split()))
ans=-1
n=len(num)
for i in range(n):
  left=i
  right=n-i-1
  if left==right:
    ans=num[i]
    break
print(ans)