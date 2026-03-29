# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.numGood = 0
        def dfs(root: TreeNode, pathMax: int):
            if not root:
                return 0
            self.numGood += 1 if root.val >= pathMax else 0
            pathMax = max(pathMax, root.val)
            l = dfs(root.left, pathMax)
            r = dfs(root.right, pathMax)
        dfs(root, root.val)
        return self.numGood
