# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root: return
            left = dfs(root.left)
            right = dfs(root.right)
            if left==right==None:
                self.res = max(self.res, root.val)
                return root.val
            if left==None:
                self.res = max(self.res, root.val+right, root.val)
                return max(root.val+right, root.val)
            if right==None:
                self.res = max(self.res, root.val+left, root.val)
                return max(root.val+left, root.val)
            self.res = max(self.res, root.val+left, root.val+right, root.val+left+right, root.val)
            return max(root.val+left, root.val+right, root.val)
        self.res = float('-inf')
        dfs(root)
        return self.res