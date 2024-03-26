# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head
        queue = []
        dummy = ListNode()
        dummy.next = head
        temp, count, start = head, 1, dummy
        while count <= right:
            if count==left-1:
                start = temp
            if left<=count<=right:
                queue.append(temp)
            temp = temp.next
            count += 1
        end = temp
        while queue:
            start.next = queue.pop()
            start = start.next
        start.next = end
        return dummy.next