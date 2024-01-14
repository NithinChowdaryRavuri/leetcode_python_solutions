"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def bfs(root):
            if not root: return
            queue = deque([root])
            while queue:
                n = len(queue)
                temp = deque()
                for _ in range(n):
                    node = queue.popleft()
                    temp.append(node)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                first = temp.popleft()
                while temp:
                    second = temp.popleft()
                    first.next = second
                    first = second
        bfs(root)
        return root