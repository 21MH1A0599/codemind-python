n=input()
v="aeiou"
l=[]
for i in n:
    if i not in l:
        if i in v:
            l.append(i)
if len(v)==len(l):
    print("True")
else:
    print("False")