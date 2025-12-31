"""
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
hash_list=[0]*11
for i in range(0,len(n)):
  hash_list[n[i]]+=1
for i in m:
  if i<1 or i>10:
    print(0)
  else:
    print(hash_list[i])
"""
'''
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
hash_dict={}
for i in n:
  hash_dict[i]=hash_dict.get(i,0)+1
print(hash_dict)

for i in m:
  print(hash_dict.get(i,0),end=" ")

'''

s='azyxyyzaaaa'
q=['d','a','y','x']
freq={}
for i in s:
  freq[i]=freq.get(i,0)+1

ans={}
for i in q:
  ans[i]=freq.get(i,0)
print(ans)