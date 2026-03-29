class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin, globalMax = nums[0],nums[0],nums[0]

        for n in nums[1:]:
            tmp = currMax * n
            currMax = max(n, tmp, n * currMin)
            currMin = min(n, n * currMin, tmp)
            globalMax = max(globalMax, currMax)
        return globalMax