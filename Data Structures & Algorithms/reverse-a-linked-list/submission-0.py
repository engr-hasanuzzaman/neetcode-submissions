# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head)
            head = head.next
        
        new_head = ListNode()
        cur_node = new_head
        while stack:
            cur_node.next = stack.pop()
            cur_node = cur_node.next
        cur_node.next = None
        return new_head.next

        