class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(numOpen: int, numClose: int, curr: List[str]):
            if numOpen == numClose == n:
                result.append(''.join(curr.copy()))
            
            if numOpen == n + 1 or numClose == n + 1:
                return
            
            if numClose > numOpen:
                return
            
            curr.append('(')
            backtrack(numOpen + 1, numClose, curr)
            curr.pop()

            curr.append(')')
            backtrack(numOpen, numClose + 1, curr)
            curr.pop()
        
        backtrack(0, 0, [])
        return result