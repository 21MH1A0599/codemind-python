n=int(input())
a,b,c,d,e,f,g,h,i=0,0,0,0,0,0,0,0,0
while n:
    r=n%10
    n//=10
    if r==1:
        a+=1
    elif r==2:
        b+=1
    elif r==3:
        c+=1
    elif r==4:
        d+=1
    elif r==5:
        e+=1    
    elif r==6:
        f+=1
    elif r==7:
        g+=1    
    elif r==8:
        h+=1
    elif r==9:
        i+=1
if a>1 or b>1 or c>1 or d>1 or e>1 or f>1 or g>1 or h>1 or i>1:
    print("Not Unique Number")
else:
    print("Unique Number")