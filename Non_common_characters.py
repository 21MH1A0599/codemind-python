s1=input().lower()
s2=input().lower()
l=''
for i in s1:
    if i not in s2 and i not in l:
        l+=i
for i in s2:
    if i not in s1 and i not in l:
        l+=i
l=l.replace(" ","")
print(len(l))