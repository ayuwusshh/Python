n=int(input())
student=[]
for _ in range(n):
  name,age,grade,gender=input().split()
  student.append((name,int(age),grade,gender))
for s in student:
  if s[1]>20:
    print(s[0],end=" ")
print()
count=0
curr_sum=0
for s in student:
  if s[3]=='Female':
    for ch in s[2]:
      curr_sum+=ord(ch)
    count+=1
print(curr_sum//count)