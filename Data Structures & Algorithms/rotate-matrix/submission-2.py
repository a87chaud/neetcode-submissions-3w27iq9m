class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        numRows = len(matrix)
        numCols = len(matrix[0])
        matrix.reverse()

        for r in range(numCols):
            for c in range(r + 1, numRows):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]