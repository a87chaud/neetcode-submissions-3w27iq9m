class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        Brute force:
        Sort array, 
        convert to set
        Keep a min val = 1, every time you see a val == min 
        val increment it.
        O(n), space = O(n)

        [1,2,4,5,2,3,6]

        '''
        nums.sort()
        numSet = set(nums)
        minVal = 1
        for n in nums:
            if n == minVal:
                minVal += 1
        
        return minVal