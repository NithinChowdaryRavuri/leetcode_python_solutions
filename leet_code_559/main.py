"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root==None:
            return 0
        depth = 0
        queue = deque([root])
        while queue:
            n = len(queue)
            depth += 1
            for _ in range(n):
                node = queue.popleft()
                if node.children!=None:
                    queue.extend(node.children)
        return depth
        