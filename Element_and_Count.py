n=int(input())
a=list(map(int,input().split()))
r=[]
for i in a:
    k=a.count(i)
    if i not in r:
        r.append(i)
        print(i,end=' ')
        print(k,end=' ')