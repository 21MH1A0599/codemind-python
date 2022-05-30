import math
n=int(input())
l=int(math.log10(n))+1
e,o,m=0,0,0
while(n):
    r=n%10
    if r%2==0:
        e+=1
    elif r%2==1:
        o+=1
    else:
        m+=1
    n//=10
if e==l:
    print('Even')
elif o==l:
    print('Odd')
else:
    print('Mixed')