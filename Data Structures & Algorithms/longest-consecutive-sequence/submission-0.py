class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for n in nums:
            currLen = 0
            while n in numSet:
                currLen += 1
                n -= 1
            maxLen = max(maxLen, currLen)
        return maxLen