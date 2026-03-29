class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i -1])
        prevSuffix = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix = prevSuffix * nums[i + 1]
            prevSuffix = suffix
            prefix[i] *= suffix
        return prefix