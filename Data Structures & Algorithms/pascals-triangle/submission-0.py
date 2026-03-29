class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for n in range(2, numRows + 1):
            new = [1] * n
            prev = res[n - 2]
            for i in range(1, len(new) - 1):
                new[i] = prev[i - 1] + prev[i]
            res.append(new)
        return res