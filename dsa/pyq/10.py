n=int(input())
nums=list(map(str,input().split()))
freq={}
for i in nums:
  freq[i]=freq.get(i,0)+1
sizes=set(s[:-1] for s in nums) # 7 8 6
pairs=0
for size in sizes:
  left=freq.get(size+'L',0)
  right=freq.get(size+'R',0)
  pairs+=min(left,right)
print(pairs)