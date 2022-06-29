n=input()
n=n.lower()
n=n.split()
v='aeiou'
f=0
r=[]
for i in n:
    c=0
    for j in i:
        if j in v:
            c+=1
    r.append(c)
for i in r:
    if i==max(r):
        f+=1
print(f)