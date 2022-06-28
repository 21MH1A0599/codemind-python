n=int(input())
a=list(map(int,input().split()))
k=int(input())
f=0
for i in a:
    if i==k:
        f=1
if f==1:
    print('True')
else:
    print('False')