s1=input()
s2=input()
s1=s1.lower()
s1=s1.replace(" ","")
s2=s2.lower()
s2=s2.replace(" ","")
l=''
for i in s1:
    for j in s2:
        if i not in l:
            if i==j:
                l+=i
l=sorted(l)
l=str(l)
l=l.replace("[","")
l=l.replace("]","")
l=l.replace(" ","")
l=l.replace("'","")
l=l.replace(",","")
if(len(l)==0):
    print("-1")
else:
    print(l)