# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if head is None:
            return False
        s = ''
        while head:
            s+=str(head.val)
            head = head.next
        return s==s[::-1]