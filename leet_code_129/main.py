# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, path=0):
            if not root: return
            path = path*10+root.val
            if root.left==root.right==None:
                self.res+=path
            dfs(root.left, path)
            dfs(root.right, path)
            path-=root.val
            path/=10
        self.res = 0
        dfs(root)
        return self.res
        