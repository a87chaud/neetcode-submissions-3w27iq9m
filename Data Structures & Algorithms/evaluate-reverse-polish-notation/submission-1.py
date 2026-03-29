class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opMap = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }
        stack = []
        for t in tokens:
            # since valid we SHOULD have the vals
            if t in opMap:
                y = int(stack.pop())
                x = int(stack.pop())
                newVal = opMap[t](x, y)
                stack.append(newVal)
            else:
                stack.append(t)
        return int(stack.pop())
