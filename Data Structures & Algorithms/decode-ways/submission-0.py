class Solution:
    def numDecodings(self, s: str) -> int:

        def dfs(index: int) -> int:
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            c1 = dfs(index + 1)
            if index < len(s) - 1:
                if s[index] == '1' or s[index] == '2' and s[index + 1] < '7':
                    c1 += dfs(index + 2)
            return c1
        return dfs(0)
            
            