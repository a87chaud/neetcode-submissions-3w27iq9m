class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(index: int, currSum: int, currList: List[int]):
            print(f'index: {index} currList: {currList}')
            if currSum == target:
                result.append(currList.copy())
                return
            if currSum > target or index == len(candidates):
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                currList.append(candidates[i])
                backtrack(i + 1, currSum + candidates[i], currList)
                currList.pop()
        
        backtrack(0, 0, [])
        return result