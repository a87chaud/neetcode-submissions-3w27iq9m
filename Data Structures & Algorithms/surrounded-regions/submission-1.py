class Solution:
    def solve(self, board: List[List[str]]) -> None:
        numRows = len(board)
        numCols = len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            # if out of range or x or # -> return
            if not 0 <= r < numRows or not 0 <= c < numCols or board[r][c] == 'X' or board[r][c] == '#':
                return
            board[r][c] = '#'

            for x, y in dirs:
                dfs(r + x, c + y)
        
        # top, bottom row
        for col in range(numCols):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[numRows - 1][col] == 'O':
                dfs(numRows - 1, col)
        
        # firsta and last col
        for row in range(numRows):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][numCols - 1] == 'O':
                dfs(row, numCols - 1)
        
        print(board)
        for row in range(numRows):
            for col in range(numCols):
                if board[row][col] == '#':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'