# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def tree_height(root):
            if root is None:
                return 0
            left = tree_height(root.left)
            right = tree_height(root.right)
            if left==-1 or right==-1 or abs(left-right)>1:
                return -1
            return 1+max(left, right)
        return tree_height(root) != -1