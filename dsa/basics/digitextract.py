n=232
m=n
print("Orignial:",n)
count=0
rev=""
cube=0
while n>0:
    rem=n%10
    rev+=str(rem)
    cube+=rem*rem*rem
    count+=1
    n=n//10
print("Count:",count)
print("Reversed:",int(rev))
if int(rev)==m:
    print('True')
else:
    print('False')
if cube==m:
    print("True")
else:
    print("False")