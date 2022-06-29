def pal(n):
    b=n[::-1]
    if n==b:
        return 1
    else:
        return 0
a=input()
a=a.lower()
a=a.split()
c=0
for i in a:
    if pal(i):
        c+=1
print(c)