class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(len(nums) - 3, -1, -1):
            print(nums)
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])
        
        return nums[0] if len(nums) == 1 else max(nums[0], nums[1])