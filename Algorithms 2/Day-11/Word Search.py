class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        visited=[[0 for _ in range(col)] for _ in range(row)]
        def dfs(r,c,ele):
            if ele==len(word):
                return True
            elif r<0 or c<0 or r>=row or c>=col or word[ele]!=board[r][c] or visited[r][c]==1:
                return False
            visited[r][c]=1
            ans=(dfs(r+1,c,ele+1) or dfs(r-1,c,ele+1) or dfs(r,c+1,ele+1) or dfs(r,c-1,ele+1))
            visited[r][c]=0
            return ans
        for i in range(row):
            for j in range(col):
                if dfs(i,j,0):
                    return True
        return False
