class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        pre=    [0, 1, 8, 11, 17, 22]
        suff =  [27, 21, 14, 11, 6, 0]
        '''
        pre = [0] * len(nums)
        suff = [0] * len(nums)

        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] + nums[i - 1]
        
        for j in range(len(nums) - 2, -1, -1):
            suff[j] = suff[j + 1] + nums[j + 1]
        
        for k in range(len(pre)):
            if pre[k] == suff[k]:
                return k
        return -1