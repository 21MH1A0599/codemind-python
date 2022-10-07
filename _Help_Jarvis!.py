n=int(input())
for i in range(n):
    s=input()
    l=[]
    for i in s:
        l.append(int(i))
    mi=min(l)
    ma=max(l)
    k=[]
    for i in range(mi,ma+1):
        k.append(i)
    if sorted(l)==sorted(k):
        print("YES")
    else:
        print("NO")