n=int(input())
s=input()
c=s.find("HH")
if c==-1:
    print("YES")
    print(s.replace(".","B"))
else:
    print("NO")