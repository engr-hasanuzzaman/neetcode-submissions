"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        store = {}
        cur = head
        while cur:
            store[cur] = Node(cur.val)
            cur = cur.next
        
        new_head = temp = Node(0)
        cur = head
        while cur:
            temp.next = store[cur]
            temp = temp.next
            if cur.next:
                temp.next = store[cur.next]
            if cur.random:
                temp.random = store[cur.random]
            cur = cur.next
        return new_head.next
        