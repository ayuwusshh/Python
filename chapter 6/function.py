add=0
def sum(n):
  if n==0:
    return
  global add
  add+=n
  sum(n-1)

sum(8)
print(add)