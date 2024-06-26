# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def bfs(root):
            queue = deque([root])
            while queue:
                node = queue.popleft()
                if node.val!=root.val:
                    self.count = min(self.count, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        self.count = float('inf')
        bfs(root)
        return self.count if self.count!=float('inf') else -1