# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        dup_head = ListNode(-1, head)
        current = dup_head
        while current.next:
            if current.next.val==val:
                current.next = current.next.next
            else:
                current = current.next
        return dup_head.next
