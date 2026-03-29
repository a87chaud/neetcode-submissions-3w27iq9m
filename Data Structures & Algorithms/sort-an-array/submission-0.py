class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        print(nums)
        if n == 1:
            return nums
        a1 = self.sortArray(nums[:n // 2])
        a2 = self.sortArray(nums[n//2:])
        return self.merge(a1, a2)
    def merge(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = 0, 0
        sort = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                sort.append(arr1[i])
                i += 1
            else:
                sort.append(arr2[j])
                j += 1
        
        while i < len(arr1):
            sort.append(arr1[i])
            i += 1
        while j < len(arr2):
            sort.append(arr2[j])
            j += 1
        return sort