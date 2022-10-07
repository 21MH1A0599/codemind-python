s1=input()
s2=input()
l=[]
k=[]
for i in s1:
    if i=='#':
        l.pop()
    else:
        l.append(i)
for i in s2:
    if i=='#':
        k.pop()
    else:
        k.append(i)
if l==k:
    print("True")
else:
    print("False")