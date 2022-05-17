class Solution:
    #check if i,j are valid in board[i][j]
    def isSafe(self,i,j,board):
        m,n=len(board),len(board[0])
        if i<0 or i>=m or j<0 or j>=n:
            return False
        return True
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #for directions top,down,left,right,and the four diagonals
        x=[-1,1,0,0,-1,1,-1,1]
        y=[0,0,-1,1,-1,1,1,-1]
        
        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                livecount=0
                for k in range(8):
                    # we need to check board[i+x[k]][j+y[k]]==1,and -1 because the board[i][j] can change the values in the other adjacent cells.
                    if self.isSafe(i+x[k],j+y[k],board) and (board[i+x[k]][j+y[k]]==1 or board[i+x[k]][j+y[k]]==-1):
                        livecount+=1
                #if the board[i][j] dies then mark it as -1
                if board[i][j]==1 and (livecount<2 or livecount>3):
                    board[i][j]=-1
                #if board[i][j] becomes live then mark it as 2
                if board[i][j]==0 and livecount==3:
                    board[i][j]=2
        #restoring the cells in terms of 0 and 1s.
        for i in range(m):
                for j in range(n):
                    if board[i][j]==2:
                        board[i][j]=1
                    
                    elif board[i][j]==-1:
                        board[i][j]=0
        return board
