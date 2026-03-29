class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroRow = [False] * len(matrix)
        zeroCol = [False] * len(matrix[0])

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeroRow[r] = True
                    zeroCol[c] = True
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if zeroRow[r] or zeroCol[c]:
                    matrix[r][c] = 0
        
        