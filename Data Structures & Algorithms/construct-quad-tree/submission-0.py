"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # base cases cond 1, 2 
        n = len(grid)
        root = Node()
        flag = True
        for r in range(n):
            for c in range(n):
                if grid[r][c] != grid[0][0]:
                    # cond2
                    root.val = 0
                    root.isLeaf = False
                    flag = False
                    break
        if flag:
            root.val = grid[0][0]
            root.isLeaf = True
            root.topRight = None
            root.topLeft = None
            root.bottomLeft = None
            root.bottomRight = None
            return root
        # split current grid into 4 subgrids and use those as the 4 children
        topLeft = []
        for r in range(0, n // 2):
            col = []
            for c in range(0, n // 2):
                col.append(grid[r][c])
            topLeft.append(col)

        topRight = []
        for r in range(0, n // 2):
            col = [] 
            for c in range(n // 2, n):
                col.append(grid[r][c])
            topRight.append(col)
        bottomLeft = []
        for r in range(n // 2, n):
            col = [] 
            for c in range(0, n // 2):
                col.append(grid[r][c])
            bottomLeft.append(col)
        bottomRight = []
        for r in range(n // 2, n):
            col = [] 
            for c in range(n // 2, n):
                col.append(grid[r][c])
            bottomRight.append(col)
        root.topLeft = self.construct(topLeft)
        root.topRight = self.construct(topRight)
        root.bottomLeft = self.construct(bottomLeft)
        root.bottomRight = self.construct(bottomRight)
        return root