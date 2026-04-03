class Solution:
    def maxScore(self, s: str) -> int:
        '''
        arr for num zeros left of curr index
        zero = [1, 1, 1, 1, 2, 2]
        arr for num zeros right of curr index
        ones = [4, 3, 2, 1, 1, 0]
        '''
        zeros = [0] * len(s)
        ones = [0] * len(s)
        zeros[0] = 1 if s[0] == '0' else 0
        for i in range(1, len(s) - 1):
            zeros[i] = zeros[i-1] + 1 if s[i] == '0' else zeros[i-1]
        
        for j in range(len(s) - 2, -1, -1):
            ones[j] = ones[j+1] + 1 if s[j+1] == '1' else ones[j+1]
        
        print(f'z: {zeros} o: {ones}')
        return max(z + o for z,o in zip(zeros, ones))
