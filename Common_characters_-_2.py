s=input().lower()
s=s.split()
a=s[0]
l=[]
for i in a:
    c=0
    for j in range(1,len(s)):
        if i in s[j]:
            c+=1
    if c==len(s)-1:
        l.append(i)
print(len(l))     