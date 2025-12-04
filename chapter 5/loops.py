tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter x: "))
for i in tup:
  if i==x:
    print('Found')
    break
else:
    print('Not found')
