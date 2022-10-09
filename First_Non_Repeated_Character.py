t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    c,d=0,0
    for i in s:
        c=0
        for j in s:
            if i==j:
                c+=1
        if c==1:
            print(i)
            d+=1
            break
    if d==0:
        print("-1")