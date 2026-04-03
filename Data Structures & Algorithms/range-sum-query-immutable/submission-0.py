class NumArray:

    def __init__(self, nums: List[int]):
        '''
        [-3, -1, -1, -4, 1, -1]
        '''
        self.nums = nums
        self.suffix = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if i + 1 < len(nums):
                self.suffix[i] = self.nums[i] + self.suffix[i+1]
            else:
                self.suffix[i] = self.nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if right + 1 < len(self.nums):
            return self.suffix[left] - self.suffix[right + 1]
        else:
            return self.suffix[left]
    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)