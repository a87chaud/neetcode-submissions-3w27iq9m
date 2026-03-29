class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(idx: int, currSum: int, curr: List[int]):
            if currSum == target:
                result.append(curr.copy())
                return
            if idx == len(nums) or currSum > target:
                return
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtrack(i, currSum + nums[i], curr)
                curr.pop()
        backtrack(0, 0, [])
        return result
                