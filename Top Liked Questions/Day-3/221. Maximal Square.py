class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        currMax = 0
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                matrix[i][j] = int(matrix[i][j])
                right = matrix[i][j+1] if j < n-1 else 0
                bottom = matrix[i+1][j] if i < m-1 else 0
                bottomRight = matrix[i+1][j+1] if j < n-1 and i < m-1 else 0
                
                if matrix[i][j] != 0:
                    matrix[i][j] = min(right, bottom, bottomRight) + 1
                
                currMax = max(currMax, matrix[i][j])

        return currMax**2
