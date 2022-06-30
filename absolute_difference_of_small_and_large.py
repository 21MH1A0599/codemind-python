n=input()
n=n.split()
for i in range(len(n)):
    a=ord(min(n[i]))
    b=ord(max(n[i]))
    print(abs(a-b),end=' ')