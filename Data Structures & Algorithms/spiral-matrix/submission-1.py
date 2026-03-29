class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []
        while top <= bottom and left <= right:
            # row = fixed @ top row, col changes
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1
            # col = fixed @ right col, row changes top -> bottom
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            if top > bottom or left > right:
                break
            # right: row = fixed @ bottom row, col = right -> left
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])    
            bottom -= 1

            # up: col fixed @ left, row = bottom -> top
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
        return result
