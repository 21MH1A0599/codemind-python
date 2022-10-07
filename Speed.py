for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n-1):
        if a[i+1]<a[i]:
            c+=1
    print(c+1)