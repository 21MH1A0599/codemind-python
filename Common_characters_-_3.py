a=input().lower()
a=a.split()
s=a[0]
c=0
l=[]
for i in s:
    c=0
    for j in range(1,len(a)):
        if i in a[j]:
            c+=1
    if c==len(a)-1:
        l.append(i)
if len(l)==0:
    print("-1")
else:
    print(min(l))