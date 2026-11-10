# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        def dfs(root):
            nonlocal best

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            # we need to return the height to root
            # so that root can calculate diameter
            # so we need to track diameter separately
            best = max(best, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return best
        