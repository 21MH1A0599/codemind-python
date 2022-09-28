n=int(input())
a=list(map(int,input().split()))
for i in range(1,20):
    if i>0:
        if i not in a:
            print(i)
            break