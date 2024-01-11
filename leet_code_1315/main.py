# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def bfs(root):
            queue = deque([root])
            res = 0
            while queue:
                node = queue.popleft()
                if node.val%2==0:
                    if node.left:
                        if node.left.left:
                            res += node.left.left.val
                        if node.left.right:
                            res += node.left.right.val
                    if node.right:
                        if node.right.left:
                            res += node.right.left.val
                        if node.right.right:
                            res += node.right.right.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return res
        return bfs(root)
        