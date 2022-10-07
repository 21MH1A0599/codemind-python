s=input()
c,d=0,0
for i in s:
    if i=='R':
        c+=1
    elif i=='L':
        c-=1
    if c==0:
        d+=1
print(d)