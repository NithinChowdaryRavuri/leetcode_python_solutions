# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res.sort()
        dummy = ListNode
        temp = dummy
        for num in res:
            temp.next = ListNode(num)
            temp = temp.next
        return dummy.next