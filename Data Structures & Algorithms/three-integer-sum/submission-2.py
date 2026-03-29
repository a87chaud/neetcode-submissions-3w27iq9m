class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        visited = set()
        startSet = set()
        for i in range(len(nums)):
            if nums[i] in startSet:
                continue
            # unique starting value
            startSet.add(nums[i])
            target = 0 - nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                currSum = nums[l] + nums[r]
                if currSum == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif currSum < target:
                    l += 1
                else:
                    r -= 1
        return result