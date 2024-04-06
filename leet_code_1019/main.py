# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        stack = []
        res = [0] * len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                res[stack.pop()] = arr[i]
            stack.append(i)
        return res