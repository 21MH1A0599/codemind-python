n=int(input())
a=list(map(int,input().split()))
s1,s2=0,0
for i in range(0,n//2):
    s1+=a[i]
for i in range(n//2,n):
    s2+=a[i]
print(s1)
print(s2)