class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(idx, curr):
            result.append(curr.copy())

            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        backtrack(0, [])
        return result