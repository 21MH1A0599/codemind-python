n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
        while a<b+1:
            r=a%10
            if r==3 or r==2 or r==9:
                c+=1
            a+=1
    print(c)           
    