for i in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    if n==1:
        print("0")
    else:
        v=[]
        for i in a:
            if i in range(1,10000000,2):
                v.append(i)
        if len(v)==0:
            print("0")
        elif len(v)%2==0:
            print(int(len(v)//2))
        else:
            print(int((len(v)-1)//2))