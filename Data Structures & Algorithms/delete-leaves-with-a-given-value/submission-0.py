# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return None
            
            if not node.left and not node.right and node.val == target:
                # delete + return
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node
        root = dfs(root)
        while root != dfs(root):
            root = dfs(root)
        return dfs(root)