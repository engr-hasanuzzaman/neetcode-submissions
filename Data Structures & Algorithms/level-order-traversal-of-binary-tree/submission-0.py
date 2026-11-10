from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            new_nodes = []
            cur_level = []
            for idx in range(len(q)):
                cur_node = q[idx]
                cur_level.append(cur_node.val)
                if cur_node.left:
                    new_nodes.append(cur_node.left)

                if cur_node.right:
                    new_nodes.append(cur_node.right)
            q = new_nodes
            ans.append(cur_level)
        return ans
                



        