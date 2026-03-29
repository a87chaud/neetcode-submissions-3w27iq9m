class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        currSum = 0
        count = 0

        for n in nums:
            currSum += n
            rem = currSum - k
            if rem in prefix:
                count += prefix[rem]
                # prefix[rem] += 1
            prefix[currSum] += 1
        return count
    

    '''
    [2, -1, 1, 2]
               ^
               r
     map = {0: 2}
    '''