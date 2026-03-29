class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if not stack or stack[-1][0] >= t:
                stack.append((t, i))
                continue
            while stack and stack[-1][0] < t:
                val, idx = stack.pop()
                res[idx] = (i - idx)
            stack.append((t, i))
        return res