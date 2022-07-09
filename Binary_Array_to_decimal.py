n=int(input())
a=list(map(int,input().split()))
a=a[::-1]
s=0
for i in range(len(a)):
    if a[i]==1:
        s+=2**i
print(s)