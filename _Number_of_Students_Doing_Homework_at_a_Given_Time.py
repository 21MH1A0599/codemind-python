n1=int(input())
a=list(map(int,input().split()))
n2=int(input())
b=list(map(int,input().split()))
x=int(input())
c=0
for i in range(0,n1):
    if a[i]<=x and b[i]>=x:
        c+=1
print(c)