class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = defaultdict(list)
        adj2 = defaultdict(list)
        # person2: [p1]
        for person1, person2 in trust:
            adj[person2].append(person1)
            adj2[person1].append(person2)
        
        for key,val in adj.items():
            if len(val) == n - 1 and len(adj2[key]) == 0:
                return key
        return -1