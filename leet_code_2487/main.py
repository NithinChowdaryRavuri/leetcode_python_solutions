# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):

        # reverse the list
        pre, cur = None, head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        # remove the node that is less than the max(greater value to the right)
        head = pre
        cur = pre.next
        max = pre.val
        while cur:
            if cur.val < max:
                pre.next = cur.next
                cur = pre.next
            else:
                max = cur.val
                pre = cur
                cur = cur.next

        # reverse the list again
        pre, cur = None, head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre