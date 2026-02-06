n=int(input())
grocery=[]
sp=total_sp=0
highestsp=""
'''
3
Pen 10 5
Book 2 100
Pencil 20 2

'''
for _ in range(n):
  item,qty,price=input().split()
  grocery.append((item,int(qty),float(price)))
for s in grocery:
  total_sp+=s[1]*s[2]
  sp=max(sp,s[1]*s[2])
for s in grocery:
  if s[1]*s[2]==sp:
    highestsp=s[0]
    break
avgsp=total_sp/n
print(highestsp)
print(int(total_sp))
print(f"{avgsp:.2f}")