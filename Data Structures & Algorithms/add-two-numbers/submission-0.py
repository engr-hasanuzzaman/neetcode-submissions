# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s_head = s_cur =  ListNode()
        rem = 0
        while l1 or l2:
            n1 = n2 = 0
            if l1:
                n1 = l1.val
                l1 = l1.next
            
            if l2:
                n2 = l2.val
                l2 = l2.next
            
            total = n1 + n2 + rem
            n_digit = total % 10
            rem = total // 10
            s_cur.next = ListNode(n_digit)
            s_cur = s_cur.next

        if rem:
            s_cur.next = ListNode(rem)
            s_cur = s_cur.next
        
        return s_head.next



        