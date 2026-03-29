class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index: int, curr: List[int]):
            if len(curr) == len(nums):
                result.append(curr.copy())

            for i in range(0, len(nums)):
                if nums[i] in curr:
                    continue
                curr.append(nums[i])
                backtrack(index + 1, curr)
                curr.pop()
        backtrack(0, [])
        return result