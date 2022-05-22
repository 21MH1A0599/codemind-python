import math
N=int(input())
for i in range(1,N+1):
    n=int(input())
    s=int(math.sqrt(n))
    if s*s==n:
         print('True')
    else:
        print('False')