class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            # print(count)
            if not 0 <= r < numRows or not 0 <= c < numCols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            total = 1
            for x, y in dirs:
                newR, newC = r + x, c + y
                total += dfs(newR, newC)
            return total
        maxArea = 0
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    print(area)
                    maxArea = max(maxArea, area)
        return maxArea