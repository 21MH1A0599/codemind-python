n=int(input())
i=0
while n:
    r=n%10
    if r>i:
        i=r
    n//=10
print(i)    
