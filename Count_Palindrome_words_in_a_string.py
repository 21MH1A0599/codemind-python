def palin(s):
    b=s[::-1]
    if s==b:
        return 1
    else:
        return 0
a=input()
a=a.lower()
a=a.split()
c=0
for i in a:
    if palin(i):
        c+=1
print(c)