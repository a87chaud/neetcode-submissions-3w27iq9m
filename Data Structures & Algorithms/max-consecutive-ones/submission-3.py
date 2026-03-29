class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        while l < len(nums) and nums[l] != 1:
            l += 1
        
        tmp = l
        max_window = 0
        for r in range(tmp, len(nums)):
            if nums[r] == 0:
                l = r + 1
            max_window = max(max_window, (r - l + 1))
        
        return max_window
            
            