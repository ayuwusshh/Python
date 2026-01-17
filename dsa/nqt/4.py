from itertools import combinations
arr = [3, 1, 2, 1, 5]
n=len(arr)
unique=set()
ans=0
for i in range(1, n + 1):
  unique.update(combinations(arr, i))
for word in unique:
  if list(word)==sorted(word) and len(list(word))==len(sorted(word)):
    ans=max(len(word),ans)
print(n-ans)
