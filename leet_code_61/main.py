# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        
        # Find the length of the linked list and the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Adjust k
        k = k % length
        
        if k == 0:
            return head
        
        # Find the new tail node
        new_tail_position = length - k - 1
        new_tail = head
        for _ in range(new_tail_position):
            new_tail = new_tail.next
        
        # Make the list circular
        tail.next = head
        
        # Update head and tail
        head = new_tail.next
        new_tail.next = None
        
        return head