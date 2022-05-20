class Solution:
    def traversal(self, matrix, dp, i, j, prev_val):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or prev_val >= matrix[i][j]:
            return 0
        
        if dp[i][j] != 0:
            return dp[i][j]
        
        up_len = self.traversal(matrix, dp, i + 1, j, matrix[i][j])
        right_len = self.traversal(matrix, dp, i, j + 1, matrix[i][j])
        down_len = self.traversal(matrix, dp, i - 1,  j, matrix[i][j])
        left_len = self.traversal(matrix, dp, i, j - 1, matrix[i][j])
        
        dp[i][j] = max(up_len, right_len, down_len, left_len) + 1
        
        return dp[i][j]
        
        
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = -1
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res = max(res, self.traversal(matrix, dp, i, j, -1))
        
        return res
