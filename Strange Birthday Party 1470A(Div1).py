t=int(input())


for _ in range(t):

    n,m=map(int,input().split())
    k=list(map(int,input().split()))
    c=list(map(int,input().split()))

    k.sort(reverse=True)

    s=0
    j=0


    for i in range(n):

        if(j<m):

            if(c[j]<c[k[i]-1]):
                s+=c[j]
                j+=1
            else:
                s+=c[k[i]-1]
        else:
            s+=c[k[i]-1]
    print(s)
