class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        numRows = len(matrix)
        numCols = len(matrix[0])

        for c in range(numCols):
            curr = []
            for r in range(numRows):
                curr.append(matrix[r][c])
            res.append(curr)
        return res