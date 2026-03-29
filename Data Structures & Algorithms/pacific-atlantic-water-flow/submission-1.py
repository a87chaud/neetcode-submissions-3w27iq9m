class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        numRows = len(heights)
        numCols = len(heights[0])
        result = []
        # visited set to see how many cells can be reached from the bottom and top
        atlantic = set() 
        pacific = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, reach, prevHeight):
            if r < 0 or r >= numRows or c < 0 or c >= numCols or heights[r][c] < prevHeight or (r, c) in reach:
                return
            reach.add((r, c))
            for x, y in dirs:
                dfs(r + x, c + y, reach, heights[r][c])
            
        for c in range(numCols):
            dfs(0, c, pacific, heights[0][c])
            dfs(numRows - 1, c, atlantic, heights[numRows - 1][c])
        
        for r in range(numRows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, numCols - 1, atlantic, heights[r][numCols - 1])
        res = []
        for row in range(numRows):
            for col in range(numCols):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        return res