s=input().lower()
s=s.split()
v='aeiou'
l=[]
for i in s:
   for j in v:
       if i not in l:
           if i.startswith(j):
               l.append(i)
print(len(l))