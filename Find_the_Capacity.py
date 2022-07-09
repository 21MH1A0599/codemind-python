a,b,c=map(int,input().split())
c=a*b*c*2*512
res=c//1024
print("%dKB"%res)