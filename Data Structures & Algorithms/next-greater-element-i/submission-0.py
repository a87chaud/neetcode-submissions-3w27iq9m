class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_map = {}
        for i, n in enumerate(nums2):
            nums2_map[n] = i
        res = [-1] * len(nums1)
        k = 0
        for n1 in nums1:
            val = -1
            print(nums2_map[n1])
            for j in range(nums2_map[n1], len(nums2)):
                if nums2[j] > n1:
                    val = nums2[j]
                    break
            res[k] = val
            k += 1
        return res