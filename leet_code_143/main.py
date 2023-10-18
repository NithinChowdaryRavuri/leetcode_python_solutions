# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None
        l = []
        temp = head
        while temp:
            l.append(temp.val)
            temp = temp.next
        i = 0
        j = len(l)-1
        temp = head
        while i<=j:
            temp.val = l[i]
            temp = temp.next
            if temp is None:
                return head
            temp.val = l[j]
            temp = temp.next
            i+=1
            j-=1
        return head