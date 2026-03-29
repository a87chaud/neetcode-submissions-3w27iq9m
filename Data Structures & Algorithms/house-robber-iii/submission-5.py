# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        robbed = {None: 0}

        def dfs(node):
            if node in robbed:
                return robbed[node]
            robbed[node] = node.val

            res = node.val
            if node.left:
                robbed[node] += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                robbed[node] += dfs(node.right.left) + dfs(node.right.right)
            
            total = max(robbed[node], dfs(node.left) + dfs(node.right))
            robbed[node] = total
            return total
        return dfs(root)