n=int(input())
lar=0
while n:
    r=n%10
    if r>lar:
        lar=r
    n//=10
print(lar)