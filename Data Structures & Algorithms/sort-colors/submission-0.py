class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3
        for n in nums:
            buckets[n] += 1
        
        numsIndex = 0
        for i, count in enumerate(buckets):
            for _ in range(count):
                nums[numsIndex] = i
                numsIndex += 1
        