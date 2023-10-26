# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        l = []
        while head:
            l.append(head.val)
            head = head.next
        i=0
        j=len(l)-1
        max = 0
        while i<j:
            temp = l[i]+l[j]
            if max<temp:
                max = temp
            i+=1
            j-=1
        return max