# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 3 cond -> current == p or q, current in between p and q: return current
        # current > p and q -> go left
        # current < p and q  -> go right
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val or min(p.val, q.val) < root.val < max(p.val, q.val):
            return root
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)