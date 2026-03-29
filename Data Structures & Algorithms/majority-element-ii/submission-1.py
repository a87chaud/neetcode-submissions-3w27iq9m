class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

            if len(count) > 2:
                new = defaultdict(int)
                for key in count.keys():
                    if count[key] > 1:
                        new[key] = count[key] - 1
                count = new
        
        res = []
        for num in count:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res
