class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        queue = deque([]) # (r, c)
        visited = set()
        fresh = 0
        for r in range(numRows):
            for c in range(numCols):
                if (r, c) not in visited and grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        level = 0
        minutes = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue and fresh > 0:
            length = len(queue)
            for _ in range(length):
                currRow, currCol = queue.popleft()
                for x,y in dirs:
                    newR, newC = currRow + x, currCol + y
                    if 0 <= newR < numRows and 0 <= newC < numCols and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        queue.append((newR, newC))
                        fresh -= 1
            minutes += 1        
        return minutes if fresh == 0 else -1