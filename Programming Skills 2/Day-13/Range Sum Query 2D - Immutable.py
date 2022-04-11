class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        y, x = len(matrix), len(matrix[0])
        if y == 0 or x == 0: return
        self.preSum = [[0 for i in range((y + 1))] for i in range(x + 1)]
        # preSum should be (x+1,y+1)
        # init the preSum with first row and first col 0(to deal with just one row or one column)
        for i in range(1, y + 1):
            for j in range(1, x + 1):
                self.preSum[i][j] = self.preSum[i-1][j] + self.preSum[i][j-1] - self.preSum[i-1][j-1] + matrix[i-1][j-1]
        # for i in range(len(self.sums)):
        #     print(self.sums[i])
        # T.C.: O(xy)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        return self.preSum[row2][col2] - self.preSum[row1-1][col2] - self.preSum[row2][col1-1] + self.preSum[row1-1][col1-1]
