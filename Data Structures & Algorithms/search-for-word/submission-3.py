class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        numRows = len(board)
        numCols = len(board[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def backtrack(row: int, col: int, wordIndex: int) -> bool:
            if wordIndex == len(word):
                return True
            if row < 0 or row >= numRows or col < 0 or col >= numCols:
                return False
            if board[row][col] != word[wordIndex] or (row, col) in visited:
                return False
            visited.add((row, col))            
            for x, y in dirs:
                newR = row + x
                newCol = col + y
                res = backtrack(newR, newCol, wordIndex + 1)
                if res:
                    return True
            visited.remove((row, col))
            return False

        for r in range(numRows):
            for c in range(numCols):
                if backtrack(r, c, 0):
                    return True
        return False

            
