# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = []
        while l1:
            first.append(str(l1.val))
            l1 = l1.next
        second = []
        while l2:
            second.append(str(l2.val))
            l2 = l2.next
        first, second = int(''.join(first)), int(''.join(second))
        res = first + second
        res = str(res)
        dummy = ListNode()
        temp = dummy
        for s in res:
            temp.next = ListNode(int(s))
            temp = temp.next
        return dummy.next