class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numSet = set()
        k = 0
        for n in nums:
            if n in numSet:
                continue
            nums[k] = n
            numSet.add(n)
            k += 1
        return k
