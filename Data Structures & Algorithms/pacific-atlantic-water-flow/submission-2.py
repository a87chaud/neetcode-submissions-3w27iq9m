class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        result = []
        numRows = len(heights)
        numCols = len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(row, col, visited, currHeight):
            if row < 0 or row >= numRows or col < 0 or col >= numCols or heights[row][col] < currHeight or (row, col) in visited:
                return
            visited.add((row, col))
            for x,y in dirs:
                dfs(row + x, col + y, visited, heights[row][col])
        # pacific: row = 0, col changes
        # atlantic: row = n - 1, col changes
        for c in range(numCols):
            dfs(0, c, pacific, heights[0][c])
            dfs(numRows - 1, c, atlantic, heights[numRows - 1][c])
        # pacific: col = 0, row changes
        # atlantic: col = n - 1, row changes
        for r in range(numRows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, numCols - 1, atlantic, heights[r][numCols - 1])
        for r, c in pacific:
            if (r, c) in atlantic:
                result.append((r,c))
        return result