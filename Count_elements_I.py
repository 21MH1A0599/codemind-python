x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
r=[]
c=0
for i in a:
    for j in b:
        if i==j:
            if i not in r:
                r.append(i)
                c+=1
print(c)