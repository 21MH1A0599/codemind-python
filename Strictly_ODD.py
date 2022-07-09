n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    if i%2==0 and a[i]%2==1:
        print('False')
        c=1
        break
if c==0:
    print('True')