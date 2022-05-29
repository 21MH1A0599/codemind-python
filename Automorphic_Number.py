n=input()
f=int(n)
s=str(f*f)
if s.endswith(n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')