# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if node.val < val -> go right
        # if node.val > val -> go left
        # if not node -> make new node and return root
        if not root:
            return TreeNode(val=val)
        
        if root.val < val:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                newNode = TreeNode(val=val)
                root.right = newNode
        if root.val > val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                newNode = TreeNode(val=val)
                root.left = newNode

        return root
