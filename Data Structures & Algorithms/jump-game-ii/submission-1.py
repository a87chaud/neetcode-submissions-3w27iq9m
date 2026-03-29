class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = deque([(nums[0], 0, 0)])

        while queue:
            curr, idx, jumps = queue.popleft()
            if idx >= len(nums) - 1:
                return jumps
            upper = min(len(nums), idx + curr + 1)
            for i in range(idx, upper):
                queue.append((nums[i], i, jumps + 1))
        
        return -1
            
