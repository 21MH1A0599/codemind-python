n=input().lower()
n=n.split()
l=''
c=0
a=n[0]
for i in a:
    c=0
    for j in range(1,len(n)):
        if i in n[j]:
            c+=1
    if c==len(n)-1:
        l+=i
if len(l)==0:
    print("-1")
else:
    print(l)