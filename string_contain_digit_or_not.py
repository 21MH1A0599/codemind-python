a=input()
s=0
for i in a:
    if i.isdigit():
        s+=1
if s>0:
    print('Contains',s,'digit')
else:
    print("Doesn't contain digit")