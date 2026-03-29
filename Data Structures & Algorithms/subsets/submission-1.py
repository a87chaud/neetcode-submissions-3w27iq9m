class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(index: int, curr: List[int]):
            result.append(curr.copy())
            
            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        backtrack(0, [])
        return result