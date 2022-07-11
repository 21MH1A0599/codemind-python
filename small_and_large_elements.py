a=input()
a=a.split()
if len(a)==2:
    print(min(a[0]),max(a[1]))
else:
    print(min(a[0]),max(a[len(a)-1]))