# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        l=[]
        while temp:
            l.append(temp.val)
            temp = temp.next
        l.sort()
        temp = head
        for num in l:
            temp.val = num
            temp = temp.next
        return head