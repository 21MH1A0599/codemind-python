n=int(input())
a=list(map(int,input().split()))
s=0
r=[]
for i in a:
    if i==a.count(i):
        if i not in r:
            r.append(i)
if len(r)==0:
    print('-1')
for i in r:
    s+=i
avg=s/len(r)
print("%.2f"%avg)