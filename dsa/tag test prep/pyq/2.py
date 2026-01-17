from itertools import permutations
n=int(input())
A=int(input())
B=int(input())
C=int(input())
s='A'*A+'B'*B+'C'*C
ans=set()
for p in permutations(s,n):
  ans.add(''.join(p))
for r in ans:
  print(r,end=" ")