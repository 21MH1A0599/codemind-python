n=int(input())
a=0
b=1
c=a+b
while(n>c):
    c=a+b
    a=b
    b=c
if(c==n):
    print('True')
else:
    print('False')