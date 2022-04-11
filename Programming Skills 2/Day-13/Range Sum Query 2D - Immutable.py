class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix) # row length
        n = len(matrix[0]) # col length
        
        # We define a presum matrix 1-col and 1-row larger than the original matrix
        # This is to tackle the boundary problem, with i,j mapped to presum[i+1][j+1]
        self.presum = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                self.presum[i][j] = matrix[i-1][j-1] + self.presum[i-1][j] + self.presum[i][j-1] - self.presum[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # The regional sum can be derived using combinations of the presum
        # We should be careful about the subscript
        return self.presum[row2+1][col2+1] + self.presum[row1][col1] - self.presum[row2+1][col1] - self.presum[row1][col2+1] 
