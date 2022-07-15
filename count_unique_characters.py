n=input()
n=n.lower()
n=n.replace(" ","")
c=0
for i in n:
    if n.count(i)==1:
        c+=1
print(c)