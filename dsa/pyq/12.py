num=list(map(int,input().split()))
freq={}
for i in num:
  freq[i]=freq.get(i,0)+1
for key,value in freq.items():
  if value>len(num)//3:
    print(key)