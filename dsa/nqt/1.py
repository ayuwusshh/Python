n=abs(int(input()))
# sumeven=False
# prodOdd=False
add=0
prod=1
s=str(n)
if len(s)<2:
  print("NO")
else:
  while(n>0):
    digit=n%10
    add+=digit
    prod*=digit
    n=n//10
if add%2==0 and prod%2!=0:
  print('YES')
else:
  print("NO")