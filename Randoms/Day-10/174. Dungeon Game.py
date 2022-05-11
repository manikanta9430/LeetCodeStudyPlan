class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        # power needed from dungeon[i][j] to dungeon[m-1][n-1]
        def dp(i: int, j: int) -> int:   
            # Base Case
            if i==m-1 and j==n-1:
                if dungeon[i][j]>=0:
                    return 1
                else:
                    return -dungeon[i][j] + 1
            
            # Out of boundary Case
            if i==m or j==n:
                return float('inf')

            # Reduce calculation
            if (memo[i][j]!=-1):
                return memo[i][j]

            # max(1, dp[i][j] + self.dungeon[i][j]) = min(dp(i,j+1),dp(i+1,j))
            res = min(dp(i,j+1),dp(i+1,j)) - dungeon[i][j]
            memo[i][j] = max(1, res)

            return memo[i][j];
        
        m = len(dungeon)
        n = len(dungeon[0])
        dungeon = dungeon
        memo = [[-1 for j in range(n)] for i in range(m)]
        return dp(0,0)
