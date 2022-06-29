n=input()
r=[]
for i in n:
    if i in 'aeiouAEIOU':
        if i not in r:
            r.append(i)
if len(r)==0:
    print('-1')
else:
    print(*r)