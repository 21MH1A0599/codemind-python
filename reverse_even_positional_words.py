a=input()
a=a.split()
for i in range(len(a)):
    if i%2==0:
        a[i]=a[i][::-1]
        print(a[i],end=' ')
    else:
        print(a[i],end=' ')
        