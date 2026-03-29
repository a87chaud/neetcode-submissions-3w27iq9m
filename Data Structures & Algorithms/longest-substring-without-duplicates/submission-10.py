class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # need a set for each substring with non-repeating chars
        # if current char is not in set, move right
        # else: set l, r to current char and clear the set
        if not s:
            return 0
        l = 0
        currSet = set()
        maxLen = 0
        for r in range(len(s)):
            if s[r] not in currSet:
                currSet.add(s[r])
                maxLen = max(r - l +1, maxLen)
                continue
            # s[r] in the set
            print(currSet)
            while l < r and s[r] in currSet and s[l] in currSet:
                currSet.remove(s[l])
                l += 1
            currSet.add(s[r])
            maxLen = max(r - l +1, maxLen)
            print(currSet)
        return maxLen
