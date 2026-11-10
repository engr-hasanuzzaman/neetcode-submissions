# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            current = stack.pop()
            if current.val == subRoot.val and self.is_same(current, subRoot):
                return True
    
            if current.left:
                stack.append(current.left)
            
            if current.right:
                stack.append(current.right)
        
        return False
        
    
    def is_same(self, r1, r2):
        if not r1 and not r2:
            return True
        
        if not r1 or not r2:
            return False
        
        if r1.val != r2.val:
            return False
        
        return self.is_same(r1.left, r2.left) and self.is_same(r1.right, r2.right)
        