n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    if a[i]%2==0 and i%2:
        print('False')
        c=1
        break
if c==0:
    print('True')