n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i
av=s/n
print("%.2f"%av)