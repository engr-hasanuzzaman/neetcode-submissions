# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        r_list = self.getRevList(head)
        size = len(r_list)
        new_head = ListNode()
        cur_node = new_head
        # print('half_size', half_size)
        for _ in range(size // 2):
            temp = head.next
            cur_node.next = head
            cur_node.next.next = r_list.pop()
            cur_node = cur_node.next.next
            head = temp
            # print('new head ', cur_node.val)

        if size % 2 == 1:
            # print('remaining node', len(r_list), len(r_list) % 2)
            # print('---s size ', len(r_list), r_li st[-1].val, cur_node.val)
            cur_node.next = r_list.pop()
            cur_node = cur_node.next
        # print('cur_node', cur_node.val)
        cur_node.next = None



    def getRevList(self, head):
        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next
        return stack
        