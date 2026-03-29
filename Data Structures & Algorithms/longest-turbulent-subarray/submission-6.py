class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        '''
        expected = odd
        [2, 4, 3, 2, 2, 5, 1, 4]

        [1, 2, 3, 4, 5, 9, 7, 8]
                        ^
                        r
                        l
        '''
        if len(arr) < 2:
            return 1
        l = 0
        maxLen = 1
        prev = -1 # 0 for less and 1 for greater
        for r in range(1, len(arr)):
            print(f'l: {arr[l]} r: {arr[r]} prev: {prev}')
            if arr[r] > arr[r-1] and prev != 1:
                # nice
                prev = 1
            elif arr[r] < arr[r-1] and prev != 0:
                # nice
                prev = 0
            else:
                # if equal -> reset
                if arr[r] == arr[r-1]:
                    l = r
                    prev = -1
                else:
                    l = r - 1
                    if arr[r] < arr[r-1]:
                        prev = 0
                    else:
                        prev = 1
            maxLen = max(maxLen, r - l + 1) 
        return maxLen