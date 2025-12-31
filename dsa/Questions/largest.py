"""nums=[55,32,-97,3,67]
large=max(nums)
print(large)"""

nums = [55, 32, -97, 3, 67]
large = nums[0]

for i in range(0, len(nums)):
    if nums[i] > large:
        large = nums[i]
print(large)
