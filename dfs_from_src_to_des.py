t=int(input())





def dfs(s,d,g,vis,path):



    vis[s]=True
    path.append(s)

    if(s==d):
        print(path)

    for i in range(len(g[s])):

        if(vis[g[s][i]]==False):
            dfs(g[s][i],d,g,vis,path)

    path.pop()
    vis[s]=False
            

for _ in range(t):

    N=int(input("Enter the number of vertices :"))

    E=int(input("Enter the number of edges :"))
    
    vis=[False]*N

    g={}

    for i in range(N):
        g[i]=[]

    for i in range(E):

        u,v=map(int,input().split())

        g[u].append(v)


        
    dfs(0,3,g,vis,[])

print(" ")

print(g)    
        
        
