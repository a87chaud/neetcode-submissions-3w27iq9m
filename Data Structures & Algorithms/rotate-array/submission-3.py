class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        print(nums)
        # reverse first k
        self.reverse(nums, 0, k-1)
        # reverse last k
        self.reverse(nums, k, len(nums) - 1)
 
        

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -= 1
        