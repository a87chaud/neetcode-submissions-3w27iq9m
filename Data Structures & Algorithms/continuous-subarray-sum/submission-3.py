class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # window size >= 2
        # sum(window) % k == 0
        # k % num = x 
        rem = {0:-1} # remainder : index
        currSum = 0
        
        for i, n in enumerate(nums):
            currSum += n
            if currSum % k not in rem:
                rem[currSum%k] = i
            elif i - rem[currSum%k] > 1:
                return True
        return False