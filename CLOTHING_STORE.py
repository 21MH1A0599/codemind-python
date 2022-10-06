n=int(input())
a=list(map(int,input().split()))
c=0
l=[]
res=0
for i in a:
    if i not in l:
        c=0
        l.append(i)
        for j in range(0,n):
            if i==a[j]:
                c+=1
        res+=c//2
print(res)