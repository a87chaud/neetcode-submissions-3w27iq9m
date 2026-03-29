# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            return 1 + max(lh, rh)
        if not root:
            return True
        lh = height(root.left)
        rh = height(root.right)
        if abs(lh - rh) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)