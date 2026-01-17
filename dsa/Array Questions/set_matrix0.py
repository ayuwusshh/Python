row,col=map(int,input().split())
nums=[list(map(int,input().split())) for _ in range(row)]
'''
4 4
07 09  02 03 ->  07, 00, 00, 03
20 08  00 10 ->  00, 00, 00, 00
29 00 -10 05 ->  00, 00, 00, 00
04 14  06 07 ->  04, 00, 00, 07
'''
r=len(nums)
c=len(nums[0])
row_track=[0]*r
col_track=[0]*c
for i in range(r):
  for j in range(c):
    if nums[i][j]==0:
      row_track[i]=-1
      col_track[j]=-1
for i in range(r):
    if row_track[i]==-1:
       for j in range(c):
              nums[i][j]=0
for j in range(c):
   if col_track[j]==-1:
      for i in range(r): 
         nums[i][j]=0
print(nums)
# def mark_infinity(nums,row,col):
#   for i in range(len(nums)):
#     if nums[i][col]!=0:
#         nums[i][col]=float('-inf')
#   for j in range(len(nums[0])):
#      if nums[row][j]!=0:
#         nums[row][j]=float('-inf')

# def set_zeroes(nums):
#   r=len(nums)
#   c=len(nums[0])
#   for i in range(r):
#      for j in range(c):
#         if nums[i][j]==0:
#            mark_infinity(nums,i,j)
#   for i in range(r):
#      for j in range(c):
#         if nums[i][j]==float('-inf'):
#            nums[i][j]=0
# set_zeroes(nums)
# print(nums,end=" ")