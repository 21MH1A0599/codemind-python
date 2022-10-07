m,n=map(int,input().split())
b=[]
for i in range(m):
    a=list(map(int,input().split()))
    b.append(a)
for i in range(n):
    s=0
    for j in range(m):
        if s<b[j][i]:
            s=b[j][i]
    print(s)