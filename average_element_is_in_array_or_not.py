n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in a:
    s+=i
avg=s//n
for i in a:
    if avg==i:
        c+=1
        break
if c==1:
    print('True');
else:
    print("False");
