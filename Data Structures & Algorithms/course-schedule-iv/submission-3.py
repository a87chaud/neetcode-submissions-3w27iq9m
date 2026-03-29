class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)

        preReqs = {} # all indirect pre, reqs

        def dfs(crs):
            if crs not in preReqs:
                preReqs[crs] = set()
                for p in adj[crs]:
                    preReqs[crs] |= dfs(p)
                
                preReqs[crs].add(crs)
            return preReqs[crs]
        for crs in range(numCourses):
            dfs(crs)
        result = []
        for u, v in queries:
            result.append(u in preReqs[v])
        return result