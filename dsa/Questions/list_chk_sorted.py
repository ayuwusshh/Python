def func(nums):
  for i in range(len(nums)-1):
    if nums[i]> nums[i+1]:
     return False
  return True
nums=[3,5,6,2,8,9,10,20]
print(func(nums))