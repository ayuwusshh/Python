n=int(input())
num=list(map(int,input().split()))
ans=""
for i in num:
  if i%15==0:
    ans+='ThreeFive'+' '
  elif i%3==0:
    ans+='Three'+' '
  elif i%5==0:
    ans+='Five'+' '
  else:
    ans+=str(i)+' '
print(ans)