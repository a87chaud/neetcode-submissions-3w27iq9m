# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # given my current node is the root of the subtree, is the subtree a valid bst
        def dfs(node, pathMin, pathMax) -> bool:
            if not node:
                return True

            ####
            if not pathMin < node.val < pathMax:
                return False
            ####
            print(f'n: {node.val} max: {pathMax} min: {pathMin}')
            pathMax = max(pathMax, node.val)
            pathMin = min(pathMin, node.val)
            return dfs(node.left, pathMin, node.val) and dfs(node.right, node.val, pathMax)
        if not root:
            return True
        return dfs(root.left, float('-inf'), root.val) and dfs(root.right, root.val, float('inf'))