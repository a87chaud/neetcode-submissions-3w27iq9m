class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = defaultdict(int)
        maxWindow = 0
        l = 0
        currSet = set()
        for r in range(len(s)):
            freqMap[s[r]] += 1
            # valid window if num replacements < k
            while (r - l + 1) - max(freqMap.values()) > k:
                freqMap[s[l]] -= 1
                l += 1
            
            maxWindow = max(maxWindow, (r - l + 1))
        return maxWindow