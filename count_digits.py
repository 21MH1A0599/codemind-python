n=int(input())
a=list(map(int,input().split()))
r=[]
for i in a:
    if i>=0:
        i=str(i)
        k=len(i)
        print(k,end=' ')
    else:
        i=str(i)
        k1=len(i)
        print(k1-1,end=' ')
        