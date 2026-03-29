class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        
        l = min(len(str1), len(str2))

        while l > 0:
            if len(str1) % l == 0 and len(str2) % l == 0:
                return str1[:l]
            l -= 1
        
        return ''