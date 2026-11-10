# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        group = 0
        cur = head
        while cur and group < k:
            cur = cur.next
            group += 1
        
        # cur.next = None
        if group == k:
            cur = self.reverseKGroup(cur, k)
            while group > 0:
                # h: 1, t: 2
                temp = head.next 
                head.next = cur
                cur = head
                head = temp
                group -= 1
            head = cur
            
        return head

        