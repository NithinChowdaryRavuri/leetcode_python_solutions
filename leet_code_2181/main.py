# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:
            if head.val == 0:
                prev = prev.next
                head = head.next
            else:
                sum = 0
                while head and head.val != 0:
                    sum += head.val
                    head = head.next
                prev.next = ListNode(sum)
        return dummy.next.next