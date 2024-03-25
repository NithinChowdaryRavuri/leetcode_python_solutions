# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head: return
        first, second = [], []
        while head:
            if head.val < x:
                first.append(head.val)
            else:
                second.append(head.val)
            head = head.next
        dummy = ListNode()
        temp = dummy
        for num in first:
            temp.next = ListNode(num)
            temp = temp.next
        for num in second:
            temp.next = ListNode(num)
            temp = temp.next
        return dummy.next