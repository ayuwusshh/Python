list1=[1,'abc','abc',1]
#list2=list(reversed(list1))
list2=list1.copy()
list2.reverse
if(list1==list2):
  print('Pallindrome')
else:
  print("Not pallindrome")