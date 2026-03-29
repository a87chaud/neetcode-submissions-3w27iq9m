class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m):
            if nums2 and nums1[i] > nums2[0]:
                tmp = nums1[i]
                minNum2 = heapq.heappop(nums2)
                nums1[i] = minNum2
                heapq.heappush(nums2, tmp)
        for j in range(m, m + n):
            nums1[j] = heapq.heappop(nums2)