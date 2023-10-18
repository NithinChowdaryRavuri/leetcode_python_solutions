"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        oldtonew = {None:None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldtonew[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = oldtonew[curr]
            copy.next = oldtonew[curr.next]
            copy.random = oldtonew[curr.random]
            curr = curr.next
        return oldtonew[head]