class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ops = {'+', 'D', 'C'}
        for o in operations:
            if o not in ops:
                stack.append(int(o))
            elif len(stack) >= 2 and o == '+':
                val1 = stack[-1]
                val2 = stack[-2]

                stack.append(val1 + val2)
            elif len(stack) >= 1 and o == 'D':
                stack.append(stack[-1] * 2)
            elif len(stack) >= 1 and o == 'C':
                stack.pop()
        return sum(stack)