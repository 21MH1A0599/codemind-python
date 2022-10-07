def uppcou(s):
    c=1
    for i in range(1,len(s)):
        if s[i].isupper():
            c+=1
    return c
s=input()
print(uppcou(s))