class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    
                    up, left = float('inf'), float('inf')
                    
                    if i > 0:
                        up = dp[i-1][j] + grid[i][j]
                    
                    if j > 0:
                        left = dp[i][j-1] + grid[i][j]
                    
                    dp[i][j] = min(up, left)
        
        return dp[n-1][m-1]
