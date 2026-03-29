class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        l = 0
        freq = defaultdict(int)
        for r in range(len(s)):
            freq[s[r]] += 1
            maxFreq = max(freq.values())

            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, (r - l + 1))
        return maxLen 