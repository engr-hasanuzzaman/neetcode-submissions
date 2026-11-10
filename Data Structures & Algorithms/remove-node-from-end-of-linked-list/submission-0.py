# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        nodes = []
        cur = head
        for _ in range(n):
            # nodes.append(cur)
            cur = cur.next
        
        nth_node = head
        while cur and cur.next:
            nth_node = nth_node.next
            cur = cur.next
        
        if not cur:
            return head.next

        if nth_node.next == head:
            return head.next
        else:
            nth_node.next = nth_node.next.next
            return head
        