n=int(input())
s=i=0
while n!=0:
    r=n%10
    s+=r*(8**i)
    n//=10
    i+=1
print("{0:b}".format(s))