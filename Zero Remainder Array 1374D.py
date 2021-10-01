t=int(input())


for _ in range(t):

    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    
    d={}


    zero=0

    
    for i in range(n):
        zz=a[i]%k
        
        if(zz==0):
            zero+=1
        else:
            zz=k-zz
            d[zz]=1+d.get(zz,0)


    maxi=0
    if(zero==n):
        print(0)

    else:

        for i in d:

            if(i==0):
                continue

            else:

                val=i

                if(d[i]-1>=1):

                    val+=(d[i]-1)*k

                maxi=max(maxi,val)
        print(maxi+1)
     
