class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        result = 0
        def backtrack(index: int, current: List[int]):
            nonlocal result
            xor = 0
            for c in current:
                xor ^= c
            result += xor
            # subsets.append(current.copy())
            for i in range(index, len(nums)):
                current.append(nums[i])
                backtrack(i+1, current)
                current.pop()
        backtrack(0, [])

        return result