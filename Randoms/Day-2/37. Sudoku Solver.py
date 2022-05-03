class Solution:
	def solveSudoku(self, board: List[List[str]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""
		n = len(board)
		m = len(board[0])

		def is_valid(row, column, val):
			for i in range(n):
				if board[i][column] == val:
					return False
			for j in range(m):
				if board[row][j] == val:
					return False
			# find square
			r = row // 3
			c = column // 3
			for i in range(r * 3, (r + 1) * 3):
				for j in range(c *  3, (c + 1) * 3):
					if board[i][j] == val:
						return False
			return True

		def is_complete():
			for i in range(n):
				for j in range(m):
					if board[i][j] == '.':
						return i, j
			return None, None

		row, column = is_complete()
		if row == column == None:
			return True

		for val in range(1, 10):
			if is_valid(row, column, str(val)):
				board[row][column] = str(val)
				if self.solveSudoku(board):
					return True
				else:
					board[row][column] = '.'


		return False # cant be 
