class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == "X":
                    if c > 0 and board[r][c-1] != ".":
                        curr_count = board[r][c-1]
                    elif r > 0 and board[r-1][c] != ".":
                        curr_count = board[r-1][c]
                    else:
                        count += 1
                        curr_count = count
                    board[r][c] = curr_count
        return count
