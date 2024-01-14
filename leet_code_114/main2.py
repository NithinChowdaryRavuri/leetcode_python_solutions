# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return
            left = dfs(root.left)
            right = dfs(root.right)
            root.left = None
            root.right = left
            node = root
            while node.right is not None:
                node = node.right
            node.right = right
            return root
        dfs(root)