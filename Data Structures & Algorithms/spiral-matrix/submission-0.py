class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        firstRow = 0
        firstCol = 0
        lastRow, m = len(matrix) - 1, len(matrix)
        lastCol, n = len(matrix[0]) - 1, len(matrix[0])
        result = []

        while firstRow <= lastRow and firstCol <= lastCol:
            # right: const = row
            print(f'firstRow: {firstRow} firstCol: {firstCol} lastRow: {lastRow} lastCol: {lastCol}')
            start, end = firstCol, lastCol
            for i in range(start, end + 1):
                result.append(matrix[firstRow][i])
            firstRow += 1
            # down: const = col
            start, end = firstRow, lastRow
            for i in range(start, end + 1):
                result.append(matrix[i][lastCol])
            lastCol -= 1

            if not (firstRow <= lastRow and firstCol <= lastCol):
                break
            # left const row
            start, end = lastCol, firstCol
            for i in range(start, end - 1, -1):
                result.append(matrix[lastRow][i])
            lastRow -= 1
            # up: const = col
            start, end = lastRow, firstRow
            for i in range(start, end - 1, -1):
                result.append(matrix[i][firstCol])
            firstCol += 1

        return result