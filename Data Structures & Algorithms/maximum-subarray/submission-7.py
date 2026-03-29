class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        [-1, -2, -3. -4]
              ^
        '''
        totalSum, subArraySum = nums[0], 0

        for i in range(0, len(nums)):
            if subArraySum < 0:
                subArraySum = 0
            subArraySum += nums[i]
            totalSum = max(subArraySum, totalSum)
        return totalSum