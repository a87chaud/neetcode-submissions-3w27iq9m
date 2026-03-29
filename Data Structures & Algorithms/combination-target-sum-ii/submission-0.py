class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(idx: int, currSum: int, curr: List[int]):
            if currSum == target:
                result.append(curr.copy())
                return
            if idx == len(candidates) or currSum > target:
                return 
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, currSum + candidates[i], curr)
                curr.pop()
                    
        backtrack(0, 0, [])
        return result