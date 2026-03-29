# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = [[root.val]]
        while queue:
            length = len(queue)
            curr = []
            for _ in range(length):
                currNode = queue.popleft()
                if currNode.left:
                    curr.append(currNode.left.val)
                    queue.append(currNode.left)
                if currNode.right:
                    curr.append(currNode.right.val)
                    queue.append(currNode.right)
            if curr:
                result.append(curr)
        return result