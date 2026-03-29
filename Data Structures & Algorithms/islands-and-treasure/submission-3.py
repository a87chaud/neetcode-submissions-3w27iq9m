class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        numRows = len(grid)
        numCols = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(row, col):
            queue = deque([(row, col, 0)])
            visited = set()
            while queue:
                currRow, currCol, level = queue.popleft()
                if grid[currRow][currCol] > 0:
                    grid[currRow][currCol] = min(level, grid[currRow][currCol])
                    visited.add((currRow, currCol))
                # print(f'r: {currRow} c: {currCol}')
                # visited.add((currRow, currCol))
                for x, y in dirs:
                    newRow, newCol = currRow + x, currCol + y
                    if 0 <= newRow < numRows and 0 <= newCol < numCols and grid[newRow][newCol] != -1 and (newRow, newCol) not in visited:
                        queue.append((newRow, newCol, level + 1))
                        visited.add((newRow, newCol))
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 0:
                    bfs(r, c)