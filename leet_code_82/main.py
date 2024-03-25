# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d, res = defaultdict(int), []
        temp = head
        while temp:
            res.append(temp.val)
            d[temp.val] += 1
            temp = temp.next
        for k in d.keys():
            if d[k] < 2:
                del d[k]
        dummy = ListNode(0)
        temp = dummy
        for val in res:
            if val in d:
                continue
            temp.next = ListNode(val)
            temp = temp.next
        return dummy.next