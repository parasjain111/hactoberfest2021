t=int(input())


for _ in range(t):
    

    n,x,m=map(int,input().split())


    ini=x
    fin=x


    for i in range(m):

        l,r=map(int,input().split())

        if(l<=ini and r>=ini):
            ini=l

        if(r>=fin and l<=fin):
            fin=r
    print(fin-ini+1)
