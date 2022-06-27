def lcm(a,b):
    c=a
    while True:
        if c%a==0 and c%b==0:
            return c
        c+=1
a,b=map(int,input().split())
res=lcm(a,b)
print(res)