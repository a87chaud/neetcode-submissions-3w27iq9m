class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(list)

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        visited = set()
        cycle = set()
        cycleStart = -1        
        # dfs 
        def dfs(node, parent):
            nonlocal cycleStart
            if node in visited:
                cycleStart = node
                return True
            visited.add(node)
            for c in graph[node]:
                if c == parent:
                    continue
                if dfs(c, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
        dfs(1, -1)

        for e1, e2 in reversed(edges):
            if e1 in cycle and e2 in cycle:
                return [e1, e2]