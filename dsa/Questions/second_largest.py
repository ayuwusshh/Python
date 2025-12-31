nums = [55, 32, -97, 3, 67]
largest=float('-inf')
second_largest=float('-inf')
for i in nums:
  if i > largest:
    second_largest=largest
    largest=i
  elif i!= largest and i>second_largest:
    second_largest=i
print(largest,second_largest)