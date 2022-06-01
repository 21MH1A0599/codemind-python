t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    c1=((n-a)//a)
    c2=((n-b)//b)
    c3=((n-(a*b))//(a*b))
    if(c1+c2-c3>k):
        print('Win')
    else:
        print('Lose')