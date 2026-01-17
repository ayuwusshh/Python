#Q1. Employee Bonus Problem
'''
A company gives bonus to employees based on performance score.
Rules:
Score ≥ 90 → bonus = 5000
Score ≥ 75 and < 90 → bonus = 3000
Score ≥ 50 and < 75 → bonus = 1000
Else → No bonus
Input:83    Output:3000
'''
# score=int(input())
# if score>=90:
#   print('5000')
# elif score>=75 and score<90:
#   print('3000')
# elif score>=50 and score<75:
#   print('1000')
# else:
#   print('No bonus')

#Q2. Fuel Station Problem
'''A car travels n km. First 10 km → ₹5 per km. Remaining → ₹3 per km
Input:18  Output:74
'''
# n = int(input())
# if n <= 10:
#     print(n * 5)
# else:
#     print(10 * 5 + (n - 10) * 3)

#Q3. Signal Jump Problem
'''A signal jumps in ste+ps: If number is even → divide by 2 
If odd → subtract 1
Count steps until number becomes 0.
Input:7 Output:5
'''
# n=int(input())
# count=0
# while n>0:
#   if n%2==0:
#     n=n//2
#   else:
#     n=n-1
#   count+=1
# print(count)

#Q4.Maximum Pair Sum
'''
Given N numbers, find maximum sum of two numbers such that:
Both numbers are even
Input:              Output: 18
6
5 2 8 3 10 7
'''
# n=int(input())
# nums=list(map(int,input().split()))
# even=[]
# for i in nums:
#   if i%2==0:
#     even.append(i)
# if len(even)<2:
#   print('-1')
# else:
#   even.sort()
#   print(even[-1]+even[-2])

# Q5.Password Validation
'''
Password is valid if:
Length ≥ 8
At least 1 uppercase At least 1 digit
Input: Abcdef12
Output: Valid
'''
# password=input('Password: ')
# has_upper=False
# has_digit=False
# if len(password)>=8:
#   for ch in password:
#     if ch.isupper():
#       has_upper=True
#     if ch.isdigit():
#       has_digit=True
#   if has_digit and has_upper:
#     print('Valid')
#   else:
#     print('Invalid')
# else:
#   print('Invalid')

#Q6. Chocolates Problem

'''A shop gives:
1 chocolate free for every 3 wrappers
Given money M and cost per chocolate C, find total chocolates.
Input:15 1  Output:22'''

# m,c=map(int,input().split())  #15 1
# tc=m//c
# wrappers=tc
# while wrappers>=3:
#   free=wrappers//3
#   tc+=free
#   wrappers=free+(wrappers%3)
# print(tc)


#Q7. Platform Tickets Problem (Logic)
'''
At a station:
Child ticket = ₹50
Adult ticket = ₹100
Input: 2 3 (2 children, 3 adults)
Output:400
'''
# c,a=map(int,input().split())
# print(c*50+100*a)