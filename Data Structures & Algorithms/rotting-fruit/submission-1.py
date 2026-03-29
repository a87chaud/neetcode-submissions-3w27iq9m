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
        
        # queue has all the rotten fruit to startt
        time = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue and fresh > 0:
            levelLength = len(queue)
            print(queue)
            for i in range(levelLength):
                row, col = queue.popleft()

                for x, y in dirs:
                    newRow = row + x
                    newCol = col + y
                    if 0 <= newRow < numRows and 0 <= newCol < numCols and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1