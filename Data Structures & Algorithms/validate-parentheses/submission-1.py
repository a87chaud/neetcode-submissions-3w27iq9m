class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for c in s:
            if c in openBrackets:
                stack.append(c)
            elif not stack and c not in openBrackets:
                return False
            else:
                top = stack.pop()
                if c != openBrackets[top]:
                    return False
        
        return len(stack) == 0