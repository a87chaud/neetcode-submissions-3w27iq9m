class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(i, curr):
            if len(curr) == k:
                result.append(curr.copy())
                return
            
            for num in range(i, n + 1):
                curr.append(num)
                backtrack(num + 1, curr)
                curr.pop()
        
        backtrack(1, [])
        return result