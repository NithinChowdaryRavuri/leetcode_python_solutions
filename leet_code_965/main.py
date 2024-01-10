# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque([root])
        res = root.val
        while queue:
            node = queue.popleft()
            if node.val!=res:
                return False
            if node.left!=None:
                queue.append(node.left)
            if node.right!=None:
                queue.append(node.right)
        return True
        