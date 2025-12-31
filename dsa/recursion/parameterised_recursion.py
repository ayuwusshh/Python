'''print x n times

def func(x,n):
  if n==0:
    return
  print(x,end=" ")
  func(x,n-1)

func(15,4)
'''
'''
1 to n using recursion

def func(n):
  if n==0:
    return
  func(n-1)
  print(n)

func(10)
'''
'''1 to n using recursion

def func(n):
  if n==0:
    return
  print(n)
  func(n-1)

func(10)'''