class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def backtracking(i,j):
            if i==m-1 and j==n-1:
                return 1
            elif i>m-1 or j>n-1:
                return 0
            return backtracking(i+1,j)+backtracking(i,j+1)
        return backtracking(0,0)
