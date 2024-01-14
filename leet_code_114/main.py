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
        def builder(out):
            if not out:
                return
            root = TreeNode(out[0])
            root.right = builder(out[1:])
            return root
        def dfs(root):
            if not root:
                return
            out.append(root.val)
            dfs(root.left)
            dfs(root.right)
        out = []
        dfs(root)
        if not out:
            return
        new = builder(out)
        root.val = new.val
        root.left = None
        root.right = new.right