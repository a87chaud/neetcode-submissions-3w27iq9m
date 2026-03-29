# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Given 2 nodes check if they are the same tree
        def sameTree(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return sameTree(node1.left, node2.left) and sameTree(node1.right, node2.right)
        if sameTree(root, subRoot):
            return True
        if root:
            l = self.isSubtree(root.left, subRoot)
            r = self.isSubtree(root.right, subRoot)
            return l or r
        else:
            return False