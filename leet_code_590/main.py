"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def post(root):
            if not root:
                return
            for child in root.children:
                post(child)
            self.res.append(root.val)
        self.res = []
        post(root)
        return self.res