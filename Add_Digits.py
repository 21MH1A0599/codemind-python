n=int(input())
sum=0
while 1:
    r=n%10
    sum+=r
    n//=10
    if n==0 and sum>9:
        n=sum
        sum=0
    elif n==0 and sum<9:
        print(sum)
        break