class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if not 0 <= r < numRows or not 0 <= c < numCols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            res = 1
            for x, y in dirs:
                res += dfs(r + x, c + y)
            return res

        maxArea = 0
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)
        
        return maxArea