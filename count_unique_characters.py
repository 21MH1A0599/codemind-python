n=input()
n=n.lower()
n=n.replace(" ","")
c=0
r=[]
for i in n:
    if n.count(i)==1:
        r.append(i)
        c+=1
print(c)