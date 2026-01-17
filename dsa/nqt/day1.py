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
arr=list(map(int,input().split()))  # 1 2 3 3
for idx in range(1,len(arr)): #2
  ls=0
  rs=0
  for i in range(0,idx):
    ls+=arr[i]#1
  for j in range(idx+1,len(arr)):
    rs+=arr[j]
  if ls==rs:
    print('Yes')
    exit()
print('No')