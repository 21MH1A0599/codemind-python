def self(n):
    c=0
    d=0
    t=n
    while n:
        r=n%10
        if r!=0 and t%r==0:
            c+=1
        n//=10
        d+=1
    if d==c:
        print(t,end=" ")
a=int(input())
b=int(input())
for i in range(a,b+1):
    self(i)
    