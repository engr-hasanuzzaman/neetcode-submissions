# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # new_head = ListNode()
        # for l in lists:
        #     new_head.next = self.merge(new_head.next, l)
        # return new_head.next
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None
                merged.append(self.merge(lists[i], l2))
            lists = merged
        
        return lists[0]



    def merge(self, l1, l2):
        # print("----calling merge")
        new_head = cur = ListNode()

        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    cur.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    cur.next = ListNode(l2.val)
                    l2 = l2.next
                cur = cur.next
            elif l1:
                cur.next = l1
                break
            else:
                cur.next = l2
                break
        # print("---returning new head ", new_head.next)
        return new_head.next
        