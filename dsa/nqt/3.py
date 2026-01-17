s=input()
freq={}
for ch in s:
  if ch in freq:
    freq[ch]+=1
  else:
    freq[ch]=1
print(freq)
mx=0
ans=''
for ch in s:
  if freq[ch]>mx:
    mx=freq[ch]
    ans=ch
print(ans)