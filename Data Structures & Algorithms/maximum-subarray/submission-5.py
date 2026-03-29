class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        [-1, -2, -3. -4]
              ^
        '''
        totalSum, subArraySum = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] >= subArraySum or subArraySum + nums[i] >= 0:
                subArraySum = max(subArraySum + nums[i], nums[i])
                totalSum = max(subArraySum, totalSum)
            else:
                subArraySum = float('-inf')
        return totalSum