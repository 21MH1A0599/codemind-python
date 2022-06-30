def rev(s):
    b=s[::-1]
    return b
n=input()
n=n.split()
for i in n:
    c=rev(i)
    print(c,end=' ')