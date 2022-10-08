n=int(input())
a=list(map(int,input().split()))
mi=min(a)
while mi>0:
    c=0
    for i in a:
        if i%mi==0:
            c+=1
    if c==n:
        print(mi)
        break
    else:
        mi-=1