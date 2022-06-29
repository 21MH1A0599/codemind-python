n=int(input())
a=list(map(int,input().split()))
s,c=0,0
for i in a:
    s+=i
av=s//n
for i in a:
    if av<=i:
        c+=1
print(c)