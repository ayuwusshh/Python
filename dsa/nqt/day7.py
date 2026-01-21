# 1
# num=list(map(int,input().split()))
# ans=-1
# for i in range(1,len(num)-1):
#   if num[i]>num[i-1] and num[i]<num[i+1]:
#     ans=num[i]
#     break
# print(ans)

#2
# s=input()
# ans=-1
# freq={}
# for i in s:
#   freq[i]=freq.get(i,0)+1
# for ch in range(1,len(s)-1):
#   if s[ch] in 'aeiou':
#     continue
#   elif freq[s[ch]]>=2 and s[ch+1]==s[ch-1]:
#     ans=s[ch]
#     break
# print(ans)

#3
num=list(map(int,input().split()))
ans=-1
for i in num:
  if i>0 and i%3!=0:
    temp=abs(i)
    add=0
    while temp>0:
      d=temp%10
      add+=d
      temp//=10
    if add%2==0:
      ans=i
      break
print(ans)