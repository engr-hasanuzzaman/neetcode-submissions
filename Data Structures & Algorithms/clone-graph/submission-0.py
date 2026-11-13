"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        memo = {}
        return self.clone(node, memo)
        # return memo[node.val]

    def clone(self, c_node, memo):
        if c_node.val in memo:
            return memo[c_node.val]
        
        memo[c_node.val] = Node(c_node.val)
    
        for n in c_node.neighbors:
            memo[c_node.val].neighbors.append(self.clone(n, memo))
        return memo[c_node.val]

        


        