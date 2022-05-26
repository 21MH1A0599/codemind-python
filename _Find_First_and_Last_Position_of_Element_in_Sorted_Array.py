n=int(input())
a=list(map(int,input().split()))
c=int(input())
f=-1
l=-1
for i in range(0,n):
    if a[i]==c and f==-1:
        f=i
    if a[i]==c:
        l=i
print(f,l)        