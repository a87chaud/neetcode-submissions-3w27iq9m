class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        count = 0
        while l <= r:
            while l <= r and nums[r] == val:
                r -= 1
                count += 1
            if nums[l] == val:
                nums[l] = nums[r]
                nums[r] = val
                r -= 1
                count += 1
            l += 1
        print(count)
        fuck = len(nums) - count
        return fuck if fuck >= 0 else 0