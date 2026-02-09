num=list(map(int,input().split()))
n=len(num)+1
actual=sum(num)
expected=(n*(n+1))//2
print(expected-actual)
