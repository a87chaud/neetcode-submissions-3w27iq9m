class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)} # e1 -> e2
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        print(graph)
        visited = set()
        def dfs(node, parent):
            # cycle
            if node in visited:
                return False
            
            # get the children and call dfs
            visited.add(node)
            children = graph[node]
            for c in children:
                if c == parent:
                    continue
                if not dfs(c, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n