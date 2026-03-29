class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        numRows = len(grid)
        numCols = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(row: int, col: int):
            queue = deque([(row, col, 0)])
            visited = {(row, col)}
            while queue:
                currRow, currCol, count = queue.popleft()
                
                if grid[currRow][currCol] > 0:
                    print(f'row: {currRow} col: {currCol} g:{grid[currRow][currCol]} count: {count}')
                    grid[currRow][currCol] = min(count, grid[currRow][currCol])
                    visited.add((currRow, currCol))
                
                for x, y in dirs:
                    newRow, newCol = currRow + x, currCol + y
                    
                    if 0 <= newRow < numRows and 0 <= newCol < numCols and (newRow, newCol) not in visited and grid[newRow][newCol] != -1:
                        queue.append((newRow, newCol, count + 1))
                        visited.add((newRow, newCol))                        
        
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == 0:
                    # visited.add((row, col))
                    print('BFS')
                    bfs(row, col)