class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1Set = set(nums1)
        num2Set = set(nums2)

        ans1 = set()
        for n1 in nums1:
            if n1 not in num2Set:
                ans1.add(n1)
        
        ans2 = set()
        for n2 in nums2:
            if n2 not in num1Set:
                ans2.add(n2)
        
        return [list(ans1), list(ans2)]