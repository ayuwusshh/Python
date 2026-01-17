#8 Bus Fare Problem
# n=int(input())
# left=n-5
# i=0
# fixed=10
# ans=0
# while i<left:
#   fixed+=2
#   i+=1
# print(fixed)

#Q9. Strong Number
# n=int(input())          #145
# ok=n
# sum=0
# fact=1
# while n>0:
#   digit=n%10      #     5
#   while digit>0:    
#     fact*=digit   #   1*5*4*3*2*1=120   4*3*2
#     digit-=1
#   sum+=fact
#   fact=1
#   n=n//10
 
# if sum==ok:
#   print("Strong")
# else:
#   print("Weak")

#Q10. Rotation Check
s1 = input().strip()
s2 = input().strip()

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes")
else:
    print("No")
