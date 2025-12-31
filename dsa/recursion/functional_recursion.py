def sum(n,x):
  if n==0:
    return x
  return sum(n-1,x+n)
print(sum(10,0))
