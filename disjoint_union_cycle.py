

def find(v):
    if(dsuf[v]==-1):
        return v
    return find(dsuf[v])




def union_op(fromP,toP):
    fromP=find(fromP)
    toP=find(toP)

    dsuf[fromP]=toP






def isCyclic(edge_list):

    for p in edge_list:

        fromP=find(p[0])
        toP=find(p[1])

        if(fromP==toP):
            return True



        union_op(fromP,toP)
        
    return False
            








E=int(input("Enter the number of edges :"))
V=int(input("Enter the number of vertices :"))

dsuf=[-1]*V

edge_list=[]

for i in range(E):
    fro,to=map(int,input().split())
    edge_list.append([fro,to])

if(isCyclic(edge_list)):
    print("TRUE")
else:
    print("FALSE")
    
