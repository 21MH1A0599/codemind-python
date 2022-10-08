n=int(input())
j=1
a=list(map(int,input().split()))
h=a[0]
for i in range(0,n):
    while j<n:
        if a[j]%h==0:
            j+=1
        else:
            h=a[j]%h
print(h)