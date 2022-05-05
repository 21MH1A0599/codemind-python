n=int(input())
sum=0
m=1
while n>0:
    r=n%10
    sum=sum+r
    m*=r
    n=n//10
sub=m-sum
print(sub)
    
