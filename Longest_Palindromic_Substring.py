def revstr(s):
    if len(s)==1:
        return s
    else:
        c=s[::-1]
        return c
s=input()
s1=''
m=0
for i in range(len(s)):
    s2=''
    for j in range(i,len(s)):
        s2+=s[j]
        if s2==revstr(s2):
            if s2 in s and len(s2)>m:
                s1=s2
                m=len(s1)
print(s1)