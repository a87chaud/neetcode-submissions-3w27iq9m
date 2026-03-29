class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        max_window = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                l = r + 1
            max_window = max(max_window, (r - l + 1))
        
        return max_window
            
            