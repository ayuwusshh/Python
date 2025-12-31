def dupli(nums):
  index=1
  for i in range(1,len(nums)):
    if nums[i]>nums[i-1]:
      index+=1
  return index
nums=[1,1,1,2,3,4,4,7,9,9,9,10]
print(dupli(nums))