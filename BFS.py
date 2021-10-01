

t=int(input())





def bfs(s,g,vis,N):


    q=[]

    q.append(s)

    vis[s]=True

    while(q!=[]):

        curr=q.pop(0)

        print(curr,end=" ")

        for i in range(0,len(g[curr])):

            if(vis[g[curr][i]]==False):
                q.append(g[curr][i])
                vis[g[curr][i]]=True

   

for _ in range(t):

    N=int(input("Enter the number of vertices :"))

    E=int(input("Enter the number of edges :"))
    
    vis=[False]*N

    g={}

    for i in range(E):

        u,v=map(int,input().split())

        if u not in g:
            g[u]=[]
            g[u].append(v)
        else:
            g[u].append(v)


        if v not in g:
            g[v]=[]
            g[v].append(u)

        else:
            g[v].append(u)

    bfs(1,g,vis,N)




        
