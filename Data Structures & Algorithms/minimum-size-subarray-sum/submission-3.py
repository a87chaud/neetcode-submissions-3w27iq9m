class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        currSum = 0
        length = len(nums) + 1
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                currSum -= nums[l]
                length = min(length, r - l + 1)
                l += 1
            
        return length if length <= len(nums) else 0
            