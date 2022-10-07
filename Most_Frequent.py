n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    k=a.count(i)
    if k not in l:
        l.append(k)
x=max(l)
y=[]
for i in a:
    if i not in y and a.count(i)==x:
        y.append(i)
print(min(y))