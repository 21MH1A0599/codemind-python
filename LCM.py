def lcm(a,b):
    c=b
    while True:
        if c%a==0 and c%b==0:
             return c
        c+=1
x,y=map(int,input().split())
print(lcm(x,y))