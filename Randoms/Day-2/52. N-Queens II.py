class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[False for i in range(n)] for j in range(n)]
        return self._helperTotalNQueens(board, 0)


    def _helperTotalNQueens(self, board, row):
        count = 0
        if row == len(board):
            count += 1
            return count

        for col in range(0, len(board)):

            if self.isSafeToPlace(board, row, col):
                board[row][col] = True
                smallCount = self._helperTotalNQueens(board, row + 1)
                count += smallCount
                board[row][col] = False
        return count

    def isSafeToPlace(self, board, row, col):

        for i in range(0, row):
            if board[i][col]:
                return False

        leftDiagMax = min(row, col)
        for i in range(1, leftDiagMax + 1):
            if board[row - i][col - i]:
                return False

        rightDiagMax = min(row, len(board) - col - 1)
        for i in range(1, rightDiagMax + 1):
            if board[row - i][col  + i]:
                return False

        return True
