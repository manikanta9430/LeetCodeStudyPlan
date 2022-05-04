class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i in obstacleGrid:
            for j in range(len(i)):
                if i[j]==0:
                    i[j]=1
                else:
                    i[j]=0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        for i in range(n):
            if obstacleGrid[0][i]==0:
                for k in range(i,n):
                    obstacleGrid[0][k]=0
                break
        for i in range(m):
            if obstacleGrid[i][0]==0:
                for k in range(i,m):
                    obstacleGrid[k][0]=0
                break
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]!=0:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]
