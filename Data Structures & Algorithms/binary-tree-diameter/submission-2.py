# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            ld = dfs(node.left)
            rd = dfs(node.right)
            diameter = max(ld + rd, diameter)
            return 1 + max(ld, rd)
        dfs(root)
        return diameter