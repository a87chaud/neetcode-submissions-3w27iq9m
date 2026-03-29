class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(row, col):
            if row < 0 or row >= numRows or col < 0 or col >= numCols or grid[row][col] == '0':
                return
            
            grid[row][col] = '0'
            for x,y in dirs:
                dfs(row + x, col + y)

        islands = 0
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        
        return islands