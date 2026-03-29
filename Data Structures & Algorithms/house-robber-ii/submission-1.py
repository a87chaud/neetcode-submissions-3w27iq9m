class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob 1st house
        if len(nums) < 2:
            return nums[0]
        if len(nums) < 3:
            return max(nums[0], nums[1])
        
        n1 = nums[:len(nums) - 1].copy()        
        n1[1] = max(n1[0], n1[1])

        for i in range(2, len(n1)):
            n1[i] = max(n1[i - 1], n1[i] + n1[i - 2])
            # print(n1)
        print(n1)
        n2 = nums[1:].copy()
        n2[1] = max(n2[1], n2[0])
        for j in range(2, len(n2)):
            n2[j] = max(n2[j - 1], n2[j] + n2[j - 2])
        print(n2)
        return max(n2[-1], n1[-1])