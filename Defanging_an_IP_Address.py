def ip(s):
    x=s.split('.')
    a=''
    b='[.]'
    a=b.join(x)
    return a
s=input()
res=ip(s)
print(res)