s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
l=''
for i in s1:
    if i not in s2 and i not in l:
        l+=i
for i in s2:
    if i not in s1 and i not in l:
        l+=i
l=sorted(l)
l=str(l)
l=l.replace("[",'')
l=l.replace("]",'')
l=l.replace(",",'')
l=l.replace("'",'')
l=l.replace(" ",'')
print(l)