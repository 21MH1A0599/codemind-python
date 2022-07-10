n=input()
n=n.split()
s1,s2=0,0
for i in n:
    mi=ord(min(i))
    s1+=mi
    ma=ord(max(i))
    s2+=ma
print(s2-s1)