# tuples are immutable lists of values

tup=(3,1,2,2,3,2)
print(type(tup))
print(tup[0]) 


# slicing works samein both tuples and lists

#tuple methods
print(tup.index(2))     #returns occurence of first occurence
print(tup.count(2))     #count total occurences