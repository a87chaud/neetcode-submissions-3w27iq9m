class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        boxSets = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                currRowSet = rowSets[row]
                currColSet = colSets[col]
                boxIndex = (row // 3 * 3) + col // 3
                currBoxSet = boxSets[boxIndex]
                currVal = board[row][col]
                if currVal in currRowSet or currVal in currColSet or currVal in currBoxSet:
                    return False
                
                if currVal != '.':
                    currRowSet.add(currVal)
                    currColSet.add(currVal)
                    currBoxSet.add(currVal)
        return True