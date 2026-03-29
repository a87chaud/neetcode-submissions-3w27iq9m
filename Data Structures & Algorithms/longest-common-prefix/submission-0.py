class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]

        for i in range(1, len(strs)):
            j, k = 0, 0
            currStr = strs[i]
            while k < len(lcp) and j < len(currStr) and lcp[k] == currStr[j]:
                k += 1
                j += 1
            lcp = lcp[:k]
        return lcp