a=input()
a=a.split()
r=[]
for i in a:
    k=len(i)
    r.append(k)
print(min(r))