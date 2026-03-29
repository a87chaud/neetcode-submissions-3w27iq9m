# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # root.val < key -> right
        # root.val > key -> left
        # if equal -> found node to delete
        if not root:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        else:
            # Im basically delete the root of this subtree
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Find the smallest value in the right subtree
            curr = root.right
            while curr.left:
                curr = curr.left
            # delete curr
            print(f'root: {root.val} curr:{curr.val}')
            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)
        return root
