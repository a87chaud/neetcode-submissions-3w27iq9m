class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numMap = {}
        for i, n in enumerate(nums):
            if n in numMap and abs(numMap[n] - i) <= k:
                return True
            numMap[n] = i
        return False