#1
# arr=list(map(int,input().split()))
# summ=0
# prod=1
# for i in arr:
#   summ+=i
#   prod*=i
# print('Sum =',summ)
# print('Product =',prod)

#2
# arr=list(map(int,input().split()))
# even=0
# odd=0
# for i in arr:
#   if i%2==0:
#     even+=1
#   else:
#     odd+=1
# print('Even =',even)
# print('Odd =',odd)

#3
# arr=list(map(int,input().split()))
# l=arr[0]
# sl=0
# for i in range(1,len(arr)):
#   if arr[i]>l:
#     sl=l
#     l=arr[i]
# print(l,sl)

#4
# arr=list(map(int,input().split()))  # 1 2 3 3
# for idx in range(0,len(arr)): #2
#   ls=0
#   rs=0
#   for i in range(0,idx):
#     ls+=arr[i]#1
#   for j in range(idx+1,len(arr)):
#     rs+=arr[j]
#   if ls==rs:
#     print('Yes')
#     exit()
# print('No')

#10
# n=int(input())
# ans=0
# while n>=10: #987
#   temp=n    #987
#   summ=0    #0
#   while(temp>0):#987  98
#     digit=temp%10  #7 8 9
#     summ+=digit #7 15 24
#     temp//=10 #98 9 0
#   n=summ  #7 15 24
#   ans=summ  # 7 15 24
# print(ans)

#11
# import math
# n,m=map(int,input().split())
# print(math.gcd(n,m))

#12
# s=input()
# arr=[]
# count=0
# for ch in s:
#   arr.append(ch)
# for i in range(len(arr)):
#   for j in range(2,i):
#     if i%j!=0:
#       count+=1
# print(count)

#13
# n=int(input())  #16
# ok=False
# while n>0:  #  16
#   if n==1:
#     ok=True
#     break
#   if n%2==0:
#     n//=2  #
#     if n==1:  #
#       ok=True
#       break
#   else:
#     break
# if ok:
#   print('YES')
# else:
#   print('NO')

#14
arr=list(map(int,input().split()))
n=len(arr)+1
add1=n*(n+1)//2
add2=sum(arr)
print(add1-add2)