class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        num_k = nums.count(k)
        num_set = set(nums)
        res = 0
        # check if every number between 1 to 50 is the sol
        for i in num_set:
            count = 0
            for num in nums:
                if num == i:
                    count += 1
                if num == k:
                    count -= 1
                count = max(count, 0)
                res = max(res, num_k + count)
        return res
                