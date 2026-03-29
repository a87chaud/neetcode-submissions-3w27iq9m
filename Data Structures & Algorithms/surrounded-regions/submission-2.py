class Solution:
    def solve(self, board: List[List[str]]) -> None:
        numRows = len(board)
        numCols = len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(row, col):
            if row < 0 or row >= numRows or col < 0 or col >= numCols or board[row][col] != 'O':
                return
            board[row][col] = 'S'

            for x, y in dirs:
                dfs(row+x, col+y)
        # r = 0, col 0 -> n
        for c in range(numCols):
            dfs(0, c)
        # col = 0, r = 0 -> n
        for r in range(numRows):
            dfs(r, 0)
        # row = n -1, 0 -> n
        for c in range(numCols - 1, -1, -1):
            dfs(numRows - 1, c)
        # col = n - 1, n - 1 -> 0
        for r in range(numRows - 1, -1, -1):
            dfs(r, numCols - 1)
        
        for r in range(numRows):
            for c in range(numCols):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'