class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW = len(board)
        COL = len(board[0])
        for r in range(ROW):
            for c in range(COL):
                if (r == 0 or c == 0 or r == ROW - 1 or c == COL - 1) and board[r][c] == 'O':
                    self.dfs(board, r, c)
        

        # enclosed
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'Y':
                    board[r][c] = 'O'
                


    def dfs(self, board, r, c):
        if r <  0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != 'O':
            return

        board[r][c] = 'Y'
        self.dfs(board, r + 1, c)
        self.dfs(board, r - 1, c)
        self.dfs(board, r, c + 1)
        self.dfs(board, r, c - 1)

        


        