n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    c=0
    for j in range(0,n):
        if a[i]==a[j]:
            c+=1
    if c>n//2:
         print(a[i],end=' ')
         break