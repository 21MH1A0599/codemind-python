def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n=int(input())
a=list(map(int,input().split()))
l=1
for i in a:
    l=l*i//gcd(l,i)
print(l)