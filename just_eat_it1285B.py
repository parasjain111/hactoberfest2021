t=int(input())


for _ in range(t):

    n=int(input())

    l=list(map(int,input().split()))
    yasser=sum(l)

    maxi=0

    max_so_far=l[0]
    max_end_here=0
    
    for i in range(0,n-1):
        max_end_here+=l[i]

        if(max_so_far<max_end_here):
            max_so_far=max_end_here

        if(max_end_here<0):
            max_end_here=0
    
    maxi=max(maxi,max_so_far)

    max_so_far=l[1]
    max_end_here=0
    for i in range(1,n):
        max_end_here+=l[i]

        if(max_so_far<max_end_here):
            max_so_far=max_end_here

        if(max_end_here<0):
            max_end_here=0

    maxi=max(maxi,max_so_far)

        
     
    if(yasser>maxi):
        print("YES")
    else:
        print("NO")
