n=input()
n=n.lower()
n=n.replace(" ","")
f=0
for i in n:
    if n.count(i)==1:
        print(i)
        f=1
        break
if f==0:
    print('-1')