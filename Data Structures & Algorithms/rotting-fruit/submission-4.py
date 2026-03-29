class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        queue = deque([])
        fresh = 0
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0
        while queue and fresh > 0:
            level = len(queue)
            for _ in range(level):
                currRow, currCol = queue.popleft()
                for x, y in dirs:
                    newRow, newCol = currRow + x, currCol + y
                    if 0 <= newRow < numRows and 0 <= newCol < numCols and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
                        fresh -= 1
            minutes += 1
        return minutes if fresh == 0 else -1