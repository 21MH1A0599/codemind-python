n=input()
a=list(n)
a=set(a)
if len(n)==len(a):
    print('Unique Number')
else:
    print('Not Unique Number')