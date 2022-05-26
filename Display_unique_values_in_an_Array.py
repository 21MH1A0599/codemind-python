n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(0,n):
    c=0
    for j in range(0,n):
        if a[i]==a[j]:
            c+=1
    if c==1:
        print(a[i],end=' ')
        count+=1
if count==0:
    print('-1')
        