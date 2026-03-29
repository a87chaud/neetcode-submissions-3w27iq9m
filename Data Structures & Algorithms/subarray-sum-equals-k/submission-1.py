class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        [2, -1, 1, 2]
        '''
        count = 0
        reqSums = {0: 1}
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            req = currSum - k

            count += reqSums.get(req, 0)
            reqSums[currSum] = 1 + reqSums.get(currSum, 0)
        return count