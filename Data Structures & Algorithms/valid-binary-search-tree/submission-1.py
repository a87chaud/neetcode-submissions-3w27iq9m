# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], minValue: int, maxValue: int) -> bool:
            if not node:
                return True
            
            if node.val <= minValue or node.val >= maxValue:
                return False

            l = dfs(node.left, minValue, node.val)
            r = dfs(node.right, node.val, maxValue)
            return l and r
        
        return dfs(root, float('-inf'), float('inf'))