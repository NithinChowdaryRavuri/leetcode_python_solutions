# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        dummy = ListNode(0, head)
        prev = head
        curr = head.next
        while prev and curr:
            temp = math.gcd(prev.val, curr.val)
            prev.next = ListNode(temp, curr)
            prev = prev.next.next
            curr = curr.next
        return dummy.next
        