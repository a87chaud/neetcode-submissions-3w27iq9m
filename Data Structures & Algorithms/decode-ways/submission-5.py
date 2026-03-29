class Solution:
    def numDecodings(self, s: str) -> int:
        mem = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                mem[i] = 0
            else:
                mem[i] = mem[i + 1]
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] < '7'):
                mem[i] += mem[i + 2]
        return mem[0]