class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        '''
        1. We need 1-26 mapping
        2. Once the number exceeds 26, it appends 
        '''
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            offset = (columnNumber % 26)
            res.append(chr(ord('A')+offset))
            columnNumber //= 26
            # res.append(chr('A') + index)
        return ''.join(reversed(res))