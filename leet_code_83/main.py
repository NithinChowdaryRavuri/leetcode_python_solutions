# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return None
        l = set()
        current = head
        l.add(current.val)
        while current.next:
            if current.next.val in l:
                current.next = current.next.next
            else:
                l.add(current.next.val)
                current = current.next
        self.tail = current
        return head