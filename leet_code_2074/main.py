# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a = []
        node = head
        while node:
            a.append(node.val)
            node = node.next
        i, d, n = 0, 1, len(a)
        while i < n:
            if min(d, n-i) & 1 == 0:
                a[i:i+d] = a[i:i+d][::-1]
            i += d
            d += 1
        node = head
        for x in a:
            node.val = x
            node = node.next
        return head
        