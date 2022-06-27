def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
a=int(input())
b=int(input())
c=0
while a<=b:
    if prime(a):
        c+=1
    a+=1
print(c)