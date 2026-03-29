class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        def dfs(row, col):
            if not 0 <= row < numRows or not 0 <= col < numCols:
                return
            if (row, col) in visited:
                return
            visited.add((row, col))
            for x, y in dirs:
                newR = row + x
                newC = col + y
                if 0 <= newR < numRows and 0 <= newC < numCols and (newR, newC) not in visited and grid[newR][newC] == '1':
                    grid[newR][newC] = '#'
                    dfs(newR, newC)
        count = 0
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] != '#' and grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        
        return count