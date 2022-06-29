a=input()
a=a.lower()
a=a.split()
v='aeiou'
r=[]
c1=0
for i in a:
    c=0
    for j in i:
        if j in v:
            c+=1
    r.append(c)
for i in r:
    if i==min(r):
        c1+=1
print(c1)