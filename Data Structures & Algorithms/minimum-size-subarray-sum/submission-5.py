class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        currSum = 0
        length = float('inf')
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                currSum -= nums[l]
                length = min(length, r - l + 1)
                l += 1
            
        return length if length != float('inf') else 0
            