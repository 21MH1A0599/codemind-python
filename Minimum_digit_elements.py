n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    i=str(i)
    k=len(i)
    b.append(k)
for i in b:
    if i==min(b):
        c+=1
print(c)
