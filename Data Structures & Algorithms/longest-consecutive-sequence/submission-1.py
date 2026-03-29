class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for n in numSet:
            curr = n + 1
            currLen = 1
            while curr in numSet:
                currLen += 1
                curr += 1
            maxLen = max(maxLen, currLen)
        return maxLen