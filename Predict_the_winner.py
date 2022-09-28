n=int(input())
a=list(map(int,input().split()))
s1,s2=0,0
for i in range(n):
    if i%2==0:
        s1+=a[i]
    else:
        s2+=a[i]
c=abs(s1-s2)
if(c%4==0):
    print("X")
else:
    print("Y")