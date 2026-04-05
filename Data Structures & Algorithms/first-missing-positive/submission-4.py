class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        Brute force:
        Sort array, 
        convert to set
        Keep a min val = 1, every time you see a val == min 
        val increment it.
        O(n), space = O(n)

        min = 1
        potential = 5
        encountered min = 3
        [3,4,-1,1]
        '''
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for j in range(n):
            val = abs(nums[j])
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                if nums[val - 1] == 0:
                    nums[val-1] = -1 * (n+1)
        
        for k in range(1,n+1):
            if nums[k-1] >= 0:
                return k
        return k+1