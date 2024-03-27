# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return
        if not head.next: return head
        if not head.next.next: return head
        first = head
        second = head.next
        dummy1 = first
        dummy2 = second
        start = head.next.next
        status = True
        while start:
            if status:
                first.next = start
                first = first.next
            else:
                second.next = start
                second = second.next
            start = start.next
            status = not status
        second.next = None
        first.next = dummy2
        return dummy1