class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])
        l, r = 0, numRows * numCols - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // numCols
            col = mid % numCols
            print(f'row: {row} col: {col} matrix: {matrix[row][col]}')
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False