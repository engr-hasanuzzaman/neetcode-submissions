# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # p < q
        def lcs(root, p, q):
            if root.val == p.val or root.val == q.val:
                return root
            
            # both values are >, check on right side
            if p.val > root.val:
                return lcs(root.right, p, q)
            elif q.val < root.val:
                return lcs(root.left, p, q)
            else:
                return root
        
        if p.val > q.val:
            return lcs(root, q, p)
        else:
            return lcs(root, p, q)

        