def self(n):
    d=0
    s=0
    temp=n
    while n:
        r=n%10
        if r!=0 and temp%r==0:
            s+=1
        n//=10
        d+=1
    if d==s:
        print(temp,end=' ')
a=int(input())
b=int(input())
for i in range(a,b+1):
    self(i)

