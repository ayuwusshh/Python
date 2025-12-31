'''
basically kya hoga ki i ko assume krenge sbse smallest number hai pure list me, ek minindex variavle lenge usko i se start krenge and ek loop chalaynge i+1 se iteration ke liye jo ki check krega ki minindex(jo ki abhi i pe hai) se agar koi chbota element hai toh uss index pe minindex ko le aao aur jb itteration khtm hoga then minindex smallest number pe khada hoga then usko swap kr lenge apne i(assumed smallest) se and fir i ko increment kr denge and minindex is back to i after every iteration
'''


nums=[5,7,8,4,1,6,9,2]
n=len(nums)
for i in range(n-1):
  minindex=i
  j=i+1
  while j<n:
    if nums[j]<nums[minindex]:
      minindex=j
    j+=1
  nums[i],nums[minindex]=nums[minindex],nums[i]
print(nums)



