class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(s)) + '#' + s for s in strs)
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            print(j)
            while s[j].isdigit():
                j += 1
            wordLen = int(s[i:j])
            word = s[j + 1: j + 1 + wordLen]
            res.append(word)
            i = j + 1 + wordLen
        return res

