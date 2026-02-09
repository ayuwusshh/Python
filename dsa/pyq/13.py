num=list(map(int,input().split()))
three=six=seven=0
for i in num:
  if i==3:
    three+=1
  elif i==6:
    six+=1
  else:
    seven+=1
num.clear()
for i in range(three):
  num.append(3)
for i in range(six):
  num.append(6)
for i in range(seven):
  num.append(7)
print(num)