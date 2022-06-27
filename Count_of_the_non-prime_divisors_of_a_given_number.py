def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
c,d=0,0
for i in range(1,n+1):
    if n%i==0:
        c+=1
        if prime(i):
            d+=1
res=c-d
print(res)
            
