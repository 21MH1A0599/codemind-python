def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
m=n
if n==2 or n==3 or n==5 or n==7 or n==1:
    print("0")
for i in range(n,2,-1):
    if prime(i):
        a=i
        break
while m!=0:
    if prime(m):
        b=m
        break
    m+=1
if n-a<b-n or n-a==b-n:
    print(n-a)
else:
    print(b-n)