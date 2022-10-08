def fac(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    return s
s=input()
s=s.split(",")
l=[]
for i in s:
    b=fac(int(i))
    if str(b) in s:
        l.append(int(i))
if len(l)==0:
    print("-1")
else:
    print(*sorted(l))