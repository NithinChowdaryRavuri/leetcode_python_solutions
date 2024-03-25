# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        n, d = 0, dict()
        while head:
            n += 1
            d[n] = head.val
            head = head.next
        dummy, c = ListNode(0), 2
        temp = dummy
        while c <= n:
            temp.next = ListNode(d[c])
            temp = temp.next
            c -= 1
            temp.next = ListNode(d[c])
            temp = temp.next
            c += 3
        if c == n+1:
            temp.next = ListNode(d[c-1])
        return dummy.next