class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_count = 0
        zero_count = 0
        l = 0
        for r in range(len(nums)):
            zero_count += 1 if nums[r] == 0 else 0
            # print(f'zero: {zero_count} l: {l} r: {r}')
            while l < r and zero_count > k:
                zero_count -= 1 if nums[l] == 0 else 0
                l += 1
            if zero_count <= k:
                max_count = max(max_count, (r - l + 1))
        return max_count