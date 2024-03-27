# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.res = []
        while head:
            self.res.append(head.val)
            head = head.next
        self.n = len(self.res)

    def getRandom(self):
        """
        :rtype: int
        """
        return self.res[random.randint(0, self.n-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()