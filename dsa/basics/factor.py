n=int(input("Enter the number: "))
i=1
arr=[]
while i<=n:
  if n%i==0:
    arr.append(i)
  i+=1
print(arr)