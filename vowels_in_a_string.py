s=input()
v=input()
f=0
for i in range(len(s)):
    if s[i]==v:
        print("True")
        print(i)
        f=1
        break
if f==0:
    print("False")