class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        strSet = set()
        for r in range(len(s)):
            while s[r] in strSet:
                print(f'r: {r} l: {l} strSet: {strSet}')
                strSet.remove(s[l])
                l += 1
            result = max(result, r - l + 1)
            strSet.add(s[r])
        return result