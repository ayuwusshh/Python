#1 sum
# num=int(input('Enter the number: '))
# sum=0
# while num!=0:
#   sum+=num%10
#   num=num//10
# print(sum)

#2 reverse
# num=int(input('ENter the number: '))
# rev=0
# while num!=0:
#   digit=num%10
#   rev=rev*10+digit
#   num=num//10
# print(rev)

#3 count vowels
# s=input("Enter the string: ").strip().lower()
# count=0
# for i in s:
#   if i=='a' or i=='e' or i=='i'or i=='o'or i=='u':
#     count+=1
# print(count)

#4 second largest
# n=int(input())
# arr=list(map(int,input().split()))
# unique=list(set(arr))
# unique.sort()
# if len(unique)<2:
#   print('0')
# else:
#   print(unique[-2])

#5
#num=int(input())
# sum=0
# while num>0:
#   digit=num%10
#   if digit%2==0:
#     sum+=digit
#   num=num//10
# print(sum)

#6 count prime
# n,m=map(int,input().split())
# count=0
# for i in range(n,m):
#   while j<=i:
#     if
# print(count)

#frequency of character
# s=input().strip()
# freq={}
# for i in s:
#   freq[i]=freq.get(i,0)+1
# for k in freq:
#     print(f"{k}:{freq[k]}", end=" ")