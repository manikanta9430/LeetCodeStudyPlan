class Solution:
    def pacificAtlantic(self, a: List[List[int]]) -> List[List[int]]:
        n=len(a)
        m=len(a[0])
        d=[[0]*m for i in range(n)]
        l=[]
        def dfs(i,j,q):
            if d[i][j]==q or d[i][j]==3:
                return
            d[i][j]+=q
            if d[i][j]==3:
                nonlocal l
                l+=[[i,j]]
            if i+1<n and a[i][j]<=a[i+1][j]:
                dfs(i+1,j,q)
            if i>0 and a[i][j]<=a[i-1][j]:
                dfs(i-1,j,q)
            if j+1<m and a[i][j]<=a[i][j+1]:
                dfs(i,j+1,q)
            if j>0 and a[i][j]<=a[i][j-1]:
                dfs(i,j-1,q)
        for i in range(n):
            dfs(i,0,1)
            dfs(i,m-1,2)
        for j in range(m):
            dfs(0,j,1)
            dfs(n-1,j,2)
        return l
