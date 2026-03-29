class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Left val, right val, operand
        [left, right] '+'
        right, left, operand -> output
        stack.push(output)
        '''
        operators = {
            '+': lambda l,r: l + r,
            '-': lambda l,r: l - r,
            '*': lambda l,r: l * r,
            '/': lambda l,r:  l / r
        }
        stack = []

        for t in tokens:
            print(stack)
            if t not in operators:
                stack.append(int(t))
            else:
                right, left = stack.pop(), stack.pop()
                val = operators[t](left, right)
                stack.append(int(val))
        return int(stack[-1])