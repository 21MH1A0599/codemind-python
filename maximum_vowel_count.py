a=input()
a=a.lower()
v='aeiou'
a=a.split()
r=[]
for i in a:
    c=0
    for j in i:
        if j in v:
            c+=1
    r.append(c)
print(max(r))