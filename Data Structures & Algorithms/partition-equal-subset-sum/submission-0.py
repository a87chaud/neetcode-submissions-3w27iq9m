class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        def dfs(index: int, currSum: int) -> bool:
            if currSum > target:
                return False
            if currSum == target:
                return True
            if index == len(nums):
                return False
            
            return dfs(index + 1, currSum + nums[index]) or dfs(index + 1, currSum)
        return dfs(0, 0)