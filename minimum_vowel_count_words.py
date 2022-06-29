n=input()
n=n.lower()
n=n.split()
r=[]
f=0
v='aeiou'
for i in n:
    c=0
    for j in i:
        if j in v:
            c+=1
    r.append(c)
for i in r:
    if i==min(r):
        f+=1
print(f)