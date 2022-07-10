n=input()
n=n.split()
for i in n:
    mi=ord(min(i))
    ma=ord(max(i))
    print(abs(mi-ma),end=' ')