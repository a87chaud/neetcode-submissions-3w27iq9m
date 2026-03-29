class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s) - 1
        while j >= 0 and s[j] == ' ':
            j -= 1
        
        # last char of last word
        count = 0
        while j >= 0 and s[j] != ' ':
            count += 1
            j -= 1
        return count