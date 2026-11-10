# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = []
        def dfs(root, max_anc_value):
            if not root:
                return
            
            if root.val >= max_anc_value:
                ans.append(root)
            
            dfs(root.left, max(max_anc_value, root.val))
            dfs(root.right, max(max_anc_value, root.val))
        
        dfs(root, float('-inf'))
        return len(ans)
        