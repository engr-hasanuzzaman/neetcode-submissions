# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = [root]
        while q:
            cur_level_nodes = []
            next_level_nodes = []
            for idx in range(len(q)):
                cur_node = q[idx]
                cur_level_nodes.append(cur_node)

                if cur_node.left:
                    next_level_nodes.append(cur_node.left)
                
                if cur_node.right:
                    next_level_nodes.append(cur_node.right)
            ans.append(cur_level_nodes.pop().val)
            q = next_level_nodes
        return ans

        