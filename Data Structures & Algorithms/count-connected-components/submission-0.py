class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        print(graph)
        visited = set()
        def dfs(node):
            # print(f'node: {node} visited: {visited}')
            if node in visited:
                return
            visited.add(node)
            for c in graph[node]:
                dfs(c)
            # visited.remove(node)
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
            # visited.clear()
        return count