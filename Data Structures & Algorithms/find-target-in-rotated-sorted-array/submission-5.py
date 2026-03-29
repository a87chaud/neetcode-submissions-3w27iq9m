class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        [1,2,3,4,5,6]
        ^    ^      ^
        
        [3,4,5,6,1,2]
        ^    ^     ^ 
        if mid > right -> move left
        move right


        [3,4,5,6,1,2]
                 ^                
        if nums[0] > target: run bin search from pivot -> len
        else: 0 -> pivot
        '''
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot = l
        print(f'pivot: {pivot}')
        if pivot != 0 and nums[0] <= target and nums[pivot - 1] >= target:
            l, r = 0, pivot - 1
        else:
            l, r = pivot, len(nums) - 1
        print(f'l: {l} r: {r}')
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


