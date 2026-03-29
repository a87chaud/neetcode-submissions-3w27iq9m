class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = 1
        decreasing = 1
        res = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                increasing, decreasing = 1, 1
            if nums[i] < nums[i + 1]:
                decreasing += 1
                increasing = 1
            if nums[i] > nums[i + 1]:
                increasing += 1
                decreasing = 1
            res = max(increasing, decreasing, res)
        return res