# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node: Optional[TreeNode], pathMax: int) -> int:
            if not node:
                return 0
            print(f'node: {node.val} path: {pathMax}')
            includeCurrent = 1 if node.val >= pathMax else 0
            pathMax = max(node.val, pathMax)            
            l = dfs(node.left, pathMax)
            r = dfs(node.right, pathMax)
            return l + r + includeCurrent
        
        return dfs(root.left, root.val) + dfs(root.right, root.val) + 1