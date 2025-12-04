marks=[92.5,22.8,95.6,'Ayush',85.6,33.75]
print(type(marks))      #list
print(marks)            # value of marks
print(len(marks))       # length of marks
marks[3]='Kumar'        # value 3rd index of marks
print(marks)            #updated value of marks
print(marks[0:4])       #slicing in list(here last index is ignored)

#list methods
print('list methods')
list=[2,1,3]
list.append(4)          #adds one value in the end
print(list)

list1=[2,1,3]
list1.sort()           #sorts in descending order
print(list1)

list2=[2,1,3]
list2.sort(reverse=True) # sorts in descending order
print(list2)

list3=[2,1,3]
list3.reverse()         #reverse the list
print(list3)

list4=[2,1,3]
list4.insert(1,5)       #insers at a given index
print(list4)