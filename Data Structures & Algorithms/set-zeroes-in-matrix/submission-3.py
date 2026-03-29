class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroCols = set()
        zeroRows = set()
        numRows = len(matrix)
        numCols = len(matrix[0])

        for r in range(numRows):
            for c in range(numCols):
                if matrix[r][c] == 0:
                    zeroCols.add(c)
                    zeroRows.add(r)
        

        for r in zeroRows:
            for c in range(numCols):
                matrix[r][c] = 0
        
        for c in zeroCols:
            for r in range(numRows):
                matrix[r][c] = 0
        