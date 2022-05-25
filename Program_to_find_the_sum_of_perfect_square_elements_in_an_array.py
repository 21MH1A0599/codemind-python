import math
n=int(input())
a=list(map(int,input().split()))
sum=0
for i in a:
    s=int(math.sqrt(i))
    if(s*s==i):
        sum+=i
print(sum)        