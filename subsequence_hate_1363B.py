t=int(input())

for _ in range(t):

    s=input()

    n=len(s)

    suf0=0
    suf1=0

    for i in range(n):

        if(s[i]=='0'):
            suf0+=1
        else:
            suf1+=1

    ans=min(suf0,suf1 )


    pref0=0
    pref1=0

    for i in range(n):

        if(s[i]=='0'):
            pref0+=1
        else:
            pref1+=1

        if(s[i]=='0'):
            suf0-=1
        else:
            suf1-=1
        ans=min(ans,pref1+suf0)
        ans=min(ans,pref0+suf1)

    print(ans)
