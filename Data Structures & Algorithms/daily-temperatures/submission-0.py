class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for index, t in enumerate(temperatures):
            counter = 0
            while stack and t > stack[-1][0]:
                curr, i = stack.pop()
                result[i] = index - i
                # print(f'stack: {stack} curr: {curr} t: {t} index: {index} counter: {counter}')
            stack.append((t, index))
        return result