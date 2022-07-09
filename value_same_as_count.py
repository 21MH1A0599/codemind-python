n=int(input())
a=list(map(int,input().split()))
r=[]
c=0
for i in a:
    if i==a.count(i):
        if i not in r:
            r.append(i)
            c+=1
print(c)
    