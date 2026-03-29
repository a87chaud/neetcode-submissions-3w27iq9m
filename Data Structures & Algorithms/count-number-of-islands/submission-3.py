class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def dfs(row, col):
            if (not 0 <= row < numRows) or (not 0 <= col < numCols) or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            for x, y in dirs:
                newR = row + x
                newC = col + y
                dfs(newR, newC)
        count = 0
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        
        return count