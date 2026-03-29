class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # pre req dict -> maps course: list of pre reqs
        prereq = {n: [] for n in range(numCourses)}
        for c, p in prerequisites:
            prereq[c].append(p)
        # Tells me if i can take my current course
        res = []
        visited = set() # All courses i can take 
        visiting = set() # My current course list(recursion stack)
        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            visiting.add(course)
            for p in prereq[course]:
                if not dfs(p):
                    return False
            visited.add(course)
            visiting.remove(course)
            res.append(course)
            return True


        for n in range(numCourses):
            if not dfs(n):
                return []
        return res