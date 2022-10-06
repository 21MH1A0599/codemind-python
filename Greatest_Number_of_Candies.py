n=int(input())
a=list(map(int,input().split()))
k=int(input())
x=max(a)
for i in a:
    if i+k>=x:
        print("True",end=' ')
    else:
        print("False",end=' ')