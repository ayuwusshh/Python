num=[5,7,3,2,6,1,5,9]
def rev(num,i=0,j=len(num)-1):
  if i>=j:
    return
  num[i],num[j]=num[j],num[i]
  rev(num,i+1,j-1)
rev(num)
print(num)