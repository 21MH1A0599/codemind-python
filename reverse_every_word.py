def rev(s):
    return s[::-1]
a=input()
a=a.split()
for i in a:
    c=rev(i)
    print(c,end=' ')