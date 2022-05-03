class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        emptyBoard = self.createBoard(n)
        fillBoard = self._helperNQueens(emptyBoard, 0)
        return fillBoard
        
    def createBoard(self, n):
        return [[ '.' for i in range(n)] for j in range(n)]

    def displayBoard(self, board):
        ans = []
        for row in board:
            temp = ''
            for el in row:
                temp += el
            ans.append(temp)
        return ans


    def isSafeToPlaceQueen(self, board, row, col):
        # Vertical Traversing
        for i in range(0, row):
            if board[i][col] == 'Q':
                return False

        # Diagonal Left Traversing
        leftMax = min(row, col)
        for i in range(1, leftMax + 1):
            if board[row - i][col - i] == 'Q':
                return False

        # Diagonal Right Traversing
        rightMax = min(row, len(board) - col - 1)
        for i in range(1, rightMax + 1):
            if board[row - i][col + i] == 'Q':
                return False

        return True


    def _helperNQueens(self, board, row):
        ans = []
        if row == len(board):
            #found one possible answer
            op = self.displayBoard(board)
            ans.append(op)
            return ans

        for col in range(0, len(board)):

            if (self.isSafeToPlaceQueen(board, row, col)):
                board[row][col] = 'Q'
                smallAns = self._helperNQueens(board, row + 1)
                ans.extend(smallAns)
                board[row][col] = '.'

        return ans
