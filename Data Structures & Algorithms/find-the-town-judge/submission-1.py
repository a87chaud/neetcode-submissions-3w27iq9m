class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degrees = [0] * (n) # 1 - n 

        # person1 -> person2(indegree+1)
        # person1 -> 
        for person1, person2 in trust:
            print(person1)
            degrees[person1-1] -= 1
            degrees[person2 - 1] += 1
        
        for i, d in enumerate(degrees):
            if d == n - 1:
                return i + 1
        return -1