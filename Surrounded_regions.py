

def mark(board,i,j,r,c):

    if(i<0 or i>r-1 or j<0 or j>c-1):
        return
    if(board[i][j]=='X'):
        return

    board[i][j]='X'

    mark(board,i-1,j,r,c)
    mark(board,i+1,j,r,c)
    mark(board,i,j-1,r,c)
    mark(board,i,j+1,r,c)


def dfs(board,i,j,r,c,visited):

    if(i<0 or i>r-1 or j<0 or j>c-1):
        return
    
    if(board[i][j]=='X' or visited[i][j]):
        return

    if(i<=0 or i>=r-1 or j<=0 or j>=c-1):
        global seen
        seen=True
   

    
    visited[i][j]=True
   
    
    dfs(board,i-1,j,r,c,visited)
    dfs(board,i+1,j,r,c,visited)
    dfs(board,i,j-1,r,c,visited)
    dfs(board,i,j+1,r,c,visited)








r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of columns:"))


board=[]

for i in range(r):
    s=input().split()
    board.append(s)

visited=[[False]*c for i in range(r)]


for i in range(1,r-1):

    for j in range(1,c-1):


        if(board[i][j]=='O' and visited[i][j]!=True):

            seen=False

            dfs(board,i,j,r,c,visited)
            print(i,j,seen)
            if(seen==False):
                
                mark(board,i,j,r,c)
            seen=True

for i in range(0,r):

    for j in range(0,c):

        print(board[i][j],end=" ")
    print(" ")


        
        
