t=int(input())





def dfs(s,g,vis):



    vis[s]=True

    print(s,end=" ")

    for i in range(len(g[s])):

        if(vis[g[s][i]]==False):
            dfs(g[s][i],g,vis)

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

    dfs(0,g,vis)

print(" ")

print(g)    
        
        
