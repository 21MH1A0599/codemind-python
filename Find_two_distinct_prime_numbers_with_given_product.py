def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
f=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if prime(i) and prime(j):
            if i<j:
                if n==i*j:
                    f=1
                    print(i,j,end=' ')
                    break
if f==0:
    print('-1')