class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # arr[i] = max(arr[i-1], dp[i-1])
        dp = [-1]*len(arr)
        for i in range(len(arr) - 2, -1, -1):
            dp[i] = max(arr[i+1], dp[i+1])
        return dp