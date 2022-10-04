n=input()
n=n.split()
for i in range(len(n)):
    for j in range(len(n)):
        if i!=j and len(n[i])<len(n[j]):
            t=n[i]
            n[i]=n[j]
            n[j]=t
print(*n)