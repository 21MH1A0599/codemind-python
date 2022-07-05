n=int(input())
a=list(map(int,input().split()))
s,c=0,0
for i in a:
    s+=i
avg=s//n
for i in a:
    if i>=avg:
        c+=1
print(c)