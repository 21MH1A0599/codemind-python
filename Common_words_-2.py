s1=input()
s2=input()
a=[]
s1=s1.lower()
s2=s2.lower()
s1=s1.split()
s2=s2.split()
for i in s1:
    for j in s2:
        if i==j:
             if s1.count(i)==1 and s2.count(j)==1:
                 a.append(i)
print(len(a))