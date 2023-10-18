# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        r = []
        if root.left:
            r+=self.inorderTraversal(root.left)
        r.append(root.val)
        if root.right:
            r+=self.inorderTraversal(root.right)
        return r