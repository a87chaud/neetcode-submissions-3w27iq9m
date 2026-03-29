class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k > len(nums):
            k = len(nums)
        for i in range(len(nums) - k + 1):
            windowMap = set()
            # print(nums[i:i+k+1])
            for i, n in enumerate(nums[i:i+k+1]):
                if n in windowMap:
                    return True
                windowMap.add(n)
            
        return False