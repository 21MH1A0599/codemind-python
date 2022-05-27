a=input()
s=0
l=len(a)
for i in range(0,l):
    if a[i]=='1':
        s+=1
    elif a[i]=='2': 
        s+=2
    elif a[i]=='3':
        s+=3
    elif a[i]=='4':
        s+=4
    elif a[i]=='5':
        s+=5
    elif a[i]=='6':
        s+=6
    elif a[i]=='7':
        s+=7
    elif a[i]=='8':
        s+=8
    elif a[i]=='9':
        s+=9
print(s)        