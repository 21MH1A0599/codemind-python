a=input()
a=a.lower()
a=a.split()
v='aeiou'
r=[]
for i in a:
    c=0
    for j in i:
        if j in v:
            c+=1
    r.append(c)
print(min(r))
            