# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        i = 0
        def reverse(pre, next):
            last = pre.next
            cur = last.next
            while cur != next:
                last.next = cur.next
                cur.next = pre.next
                pre.next = cur
                cur = last.next
            return last
        while head:
            i += 1
            if i % k == 0:
                pre = reverse(pre, head.next)
                head = pre.next
            else:
                head = head.next
        return dummy.next
        