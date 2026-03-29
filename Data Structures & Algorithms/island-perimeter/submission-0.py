class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        perimeter = 0
        def dfs(row, col):
            nonlocal perimeter
            if not 0 <= row < numRows or not 0 <= col < numCols or grid[row][col] == 0:
                return 1
            
            if (row, col) in visited:
                return 0

            visited.add((row, col))
            res = 0
            for x, y in dirs:
                newRow, newCol = row + x, col + y
                res += dfs(newRow, newCol)
            return res
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 1:
                    return dfs(r, c)
        return perimeter