class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for r in range(len(nums)):
            rightSum = total - nums[r] - leftSum
            if leftSum == rightSum:
                return r
            leftSum += nums[r]
        
        return -1