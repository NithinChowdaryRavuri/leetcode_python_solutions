# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque([root])
        Even = True
        while queue:
            n = len(queue)
            prev = None
            for _ in range(n):
                node = queue.popleft()
                if Even:
                    if node.val%2==0:
                        return False
                    if prev: 
                        if node.val <= prev:
                            return False
                    prev = node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    if node.val%2!=0:
                        return False
                    if prev: 
                        if node.val >= prev:
                            return False
                    prev = node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            Even = not Even
        return True