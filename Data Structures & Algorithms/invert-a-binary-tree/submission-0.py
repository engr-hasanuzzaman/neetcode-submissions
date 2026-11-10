# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root

        new_left = new_right = None
        if root.right:
            new_left = self.invertTree(root.right)
        
        if root.left:
            new_right = self.invertTree(root.left)
        
        root.left = new_left
        root.right = new_right
        return root

        