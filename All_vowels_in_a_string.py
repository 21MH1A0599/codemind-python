n=input()
v='aeiou'
c=[]
for i in n:
    if i in v and i not in c:
        c.append(i)
if len(c)==len(v):
    print("True")
else:
    print("False")