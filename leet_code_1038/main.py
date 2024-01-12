# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            root.val+=self.res
            self.res = root.val
            dfs(root.left)
        self.res=0
        dfs(root)
        return root
        