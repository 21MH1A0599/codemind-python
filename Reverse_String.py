a=input()
a=a.split()
n=len(a)
r=[]
for i in range(n-1,-1,-1):
    r.append(a[i])
print(*r)