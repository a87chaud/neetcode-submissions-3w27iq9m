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
                maxLen = max(maxLen, r - l + 1) 
                prev = 1
            elif arr[r] < arr[r-1] and prev != 0:
                # nice
                maxLen = max(maxLen, r - l + 1) 
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


        # for r in range(1, len(arr)):
        #     if arr[r] == arr[r-1]:
        #         l = r
        #         expected = -1
        #     elif arr[r] < arr[r - 1] and expected == 1:
        #         l = r - 1
        #         expected = -1
        #     elif arr[r] > arr[r - 1] and expected == 0:
        #         l = r - 1
        #         expected = -1
        #     else:
        #         if arr[r] < arr[r - 1]:
        #             expected = 1
        #         else:
        #             expected = 0
        #     maxLen = max(maxLen, r - l + 1) 
        #     print(f'l: {l} r: {r} nums: {arr[r]} expected: {expected}')
        return maxLen