# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        temp = head
        l = 0
        while temp:
            l+=1
            temp = temp.next
        dummy = ListNode(0,head)
        front = back = dummy
        v = k-1
        while v>0:
            front = front.next
            v-=1
        v = l-k
        while v>0:
            back = back.next
            v-=1
        front.next.val, back.next.val = back.next.val, front.next.val
        return head