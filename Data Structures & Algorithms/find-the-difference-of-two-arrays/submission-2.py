class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1Set = set(nums1)
        num2Set = set(nums2)
        ans1, ans2 = [], []

        for num in num1Set:
            if num not in num2Set:
                ans1.append(num)
        
        for num in num2Set:
            if num not in num1Set:
                ans2.append(num)
        
        return [ans1, ans2]