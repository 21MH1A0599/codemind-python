def per(s,ans):
    if len(s)==0:
        print(ans)
        return
    for i in range(len(s)):
        ch=s[i]
        l_s=s[0:i]
        r_s=s[i+1:]
        re=l_s+r_s
        per(re,ans+ch)
ans=''
s=input()
per(s,ans)