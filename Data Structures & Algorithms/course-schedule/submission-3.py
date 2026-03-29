class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqs = {n: [] for n in range(numCourses)}
        for course, pre in prerequisites:
            preReqs[course].append(pre)
        print(preReqs)
        def dfs(visited, course):
            print(f'visited: {visited} course: {course}')
            if course in visited:
                print('lol')
                return False
            if not preReqs[course]:
                return True
            visited.add(course)
            for c in preReqs[course]:
                if not dfs(visited, c):
                    return False
            visited.remove(course)
            return True
        
        for n in range(numCourses):
            res = dfs(set(), n)
            print(res)
            if not res:
                return False
        return True
        