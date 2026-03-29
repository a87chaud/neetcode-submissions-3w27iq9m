class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []

        def backtrack(index: int, current: List[int]):
            subsets.append(current.copy())
            for i in range(index, len(nums)):
                current.append(nums[i])
                backtrack(i+1, current)
                current.pop()
        backtrack(0, [])

        result = 0
        for s in subsets:
            if not s:
                continue
            if len(s) < 2:
                result += s[0]
                continue
            x1 = s[0]
            x2 = s[1]
            stack = []
            stack.append(x1 ^ x2)
            for i in range(2, len(s)):
                prev = stack.pop()
                stack.append(s[i] ^ prev)
            print(stack)
            result += stack[0]
        return result