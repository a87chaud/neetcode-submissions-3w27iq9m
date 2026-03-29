class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        numRows = len(grid)
        numCols = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(row: int , col: int):
            queue = deque([(row, col, 0)])
            visited = set()
            while queue:
                currRow, currCol, dist = queue.popleft()
                if grid[currRow][currCol] > 0:
                    grid[currRow][currCol] = min(grid[currRow][currCol], dist)
                    visited.add((currRow, currCol))
                for x,y in dirs:
                    newRow = currRow + x
                    newCol = currCol + y

                    if 0 <= newRow < numRows and 0 <= newCol < numCols and (newRow, newCol) not in visited and grid[newRow][newCol] > 0:
                        queue.append((newRow, newCol, dist + 1))
                        visited.add((newRow, newCol))

        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 0:
                    bfs(r, c)