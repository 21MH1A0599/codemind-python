a=int(input())
c=0
for i in range(0,a):
    n=input()
    for j in n:
        if j=='+':
            c+=1
    else:
         c-=1
print(c)