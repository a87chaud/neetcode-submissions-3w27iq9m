class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainderMap = {}

        for i, n in enumerate(nums):
            if n in remainderMap:
                return [remainderMap[n], i]
            remainder = target - n
            remainderMap[remainder] = i
        return [-1, -1]