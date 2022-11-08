s1=input().lower()
s2=input().lower()
l=[]
for i in s1:
    for j in s2:
        if i==j and i not in l:
            l.append(i)
l.sort()
l=str(l)
l=l.replace(" ","")
l=l.replace("[","")
l=l.replace("]","")
l=l.replace(",","")
l=l.replace("'","")
if len(l)==0:
    print("-1")
else:
    print(l)