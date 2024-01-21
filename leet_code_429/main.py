"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque([root])
        res= []
        while queue:
            n = len(queue)
            temp = []
            for _ in range(n):
                node = queue.popleft()
                temp.append(node.val)
                for children in node.children:
                    queue.append(children)
            res.append(temp)
        return res