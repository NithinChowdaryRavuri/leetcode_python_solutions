# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        res = dummy
        while head:
            curr = head.val
            curr *= 2
            if curr > 9:
                dummy.val += 1
                curr -= 10
            head.val = curr
            dummy = dummy.next
            head = head.next
        if res.val == 0:
            return res.next
        else: return res
            