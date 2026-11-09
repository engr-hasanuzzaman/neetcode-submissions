# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        cur_node = new_head

        while list1 or list2:
            # print(new_head.val)
            if list1 and list2:
                # print('----both has value')
                if list1.val < list2.val:
                    cur_node.next = list1
                    list1 = list1.next
                else:
                    cur_node.next = list2
                    list2 = list2.next
                cur_node = cur_node.next
            elif list1:
                while list1:
                    cur_node.next = list1
                    list1 = list1.next
                    cur_node = cur_node.next
            else:
                while list2:
                    cur_node.next = list2
                    list2 = list2.next
                    cur_node = cur_node.next
        return new_head.next


        