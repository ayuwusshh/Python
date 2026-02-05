#1
# num=list(map(int,input().split()))
# n=len(num)
# ans=-1
# avgg=sum(num)/n
# for i in range(n):
#   if num[i]%2!=0 and num[i]>avgg:
#     temp=abs(num[i])
#     if temp==0:
#       count=1
#     else:
#       count=0
#       while temp>0:
#         temp//=10
#         count+=1
#     if count%2==0:
#       ans=num[i]
#       break
# print(ans)

#2
# s=input()
# ans=-1
# freq={}
# for ch in s:
#   freq[ch]=freq.get(ch,0)+1
# for ch in range(1,len(s)-1):
#   if s[ch].isalpha() and freq[s[ch]]==2 and (ord(s[ch-1])+ord(s[ch+1]))%2==0:     
#       ans=s[ch]
#       break
# print(ans)

#3
# num=list(map(int,input().split()))
# n=len(num)
# left=0
# ans=-1
# total=sum(num)
# for i in range(n):
#   right=total-left-num[i]
#   if left==right:
#     ans=num[i]
#     break
#   else:
#     left+=num[i]
# print(ans)