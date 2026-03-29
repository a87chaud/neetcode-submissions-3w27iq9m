class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index: int, currSum: int, currList: List[int]):
            if currSum == target:
                result.append(currList.copy())
                return
            if currSum > target:
                return 
            
            if index == len(nums):
                return
            
            for i in range(index, len(nums)):
                currList.append(nums[i])
                x = currSum + nums[i]
                backtrack(i, x, currList)
                currList.pop()
        
        backtrack(0, 0, [])
        return result