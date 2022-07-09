def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.2)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
f=0
for i in range(1,n):
    for j in range(1,n):
        if prime(i) and prime(j):
            if i*j==n:
                if i<j:
                    f=1
                    print(i,j)
                    break
if f==0:
    print('-1')