a=input()
a=a.lower()
a=a.split()
v='aeiou'
c1=0
r=[]
for i in a:
    c=0
    for j in i:
        if j in v:
            c+=1
    r.append(c)
for i in r:
    if i==max(r):
        c1+=1
print(c1)