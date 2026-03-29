class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0: -1}
        currSum = 0
        for r in range(len(nums)):
            currSum += nums[r]
            rem = currSum % k
            if rem not in prefix:
                prefix[rem] = r
            if rem in prefix and r - prefix[rem] > 1:
                return True
        return False
