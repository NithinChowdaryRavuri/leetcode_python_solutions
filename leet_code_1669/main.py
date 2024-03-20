# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        count, link1, link2 = 0, ListNode(), ListNode()
        head = list1
        while count<=b:
            if count == a-1:
                link1 = head
            elif count == b:
                link2 = head
            head = head.next
            count += 1
        link1.next, tail2.next = list2, link2.next
        return list1
        