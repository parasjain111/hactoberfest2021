
def isCyclic_util(graph,visited,curr):

    if(visited[curr]==True):
        return True

    visited[curr]=True

    FLAG=False
   
    for i in range(len(graph[curr])):

        FLAG=isCyclic_util(graph,visited,graph[curr][i])
        
        
        
        if(FLAG==True):
            
            return True
    
    return False



def isCyclic(V,graph):
    visited=[False]*V
    flag=False

   
    for i in range(V):
        visited[i]=True
        
        for j in range(len(graph[i])):

            flag=isCyclic_util(graph,list(visited),graph[i][j])
         
            if(flag==True):
                
                return True
        visited[i]=False
        
    return False





t=int(input("Enter the number of test cases: "))

for _ in range(t):

    v=int(input("Enter the numbers of vertices :"))

    e=int(input("Enter the number of edges:"))

    graph={}
    
    for i in range(v):
        graph[i]=[]

    for i in range(e):
        # initial: initial node , final: final node
        initial,final=map(int,input().split())
        graph[initial].append(final)
  
        
    print(graph)

    res=isCyclic(v,graph)
    if(res==True):
        print("There exists a cycle")
    else:
        print("There is no cycle")
              
