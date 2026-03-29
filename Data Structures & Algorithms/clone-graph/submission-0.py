"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque([node])
        oldToNew = {}

        while queue:
            old = queue.popleft()
            if old.val in oldToNew:
                new = oldToNew[old.val]
            else:
                new = Node(old.val)
                oldToNew[old.val] = new
            # print(f'val: {old.val} old: {old} new: {new} oldToNew: {oldToNew}')
            for n in old.neighbors:
                print(n.val)
                if n.val in oldToNew:
                    new.neighbors.append(oldToNew[n.val])
                else:
                    queue.append(n)
                    newN = Node(n.val)
                    new.neighbors.append(newN)
                    oldToNew[n.val] = newN
            
        return oldToNew[1]
